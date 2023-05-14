import pandas as pd

#f_1_0, f_1_1, f_1_2, i_1_2, f_4_2, f_3_0, f_5_1, i_4_1, i_5_2, f_3_2, i_2_0, i_4_0, i_2_1, i_4_1
# Read Excel file
data = pd.read_excel('15.xlsx', dtype={'Subtopic': int, 'Number': int, 'Duration': int, 'Value': int, 'Mandatory': int })
Kmin = 70
Kmax = 90
activities = []
for index, row in data.iterrows():
    activity = {
        'subtopic': row['Subtopic'],
        'number': row['Number'],
        'duration': row['Duration'],
        'value': row['Value'],
        'mandatory': row['Mandatory'],
        'requirement1': row['Requirement 1'],
        'requirement2': row['Requirement 2']
    }
    activities.append(activity)

def convert_requirements_to_mandatory(activity):
    requirement1 = activity['requirement1']
    requirement2 = activity['requirement2']
    if requirement1:
        requirement1_activity = next(a for a in activities if a['number'] == requirement1)
        requirement1_activity['mandatory'] = 1
        convert_requirements_to_mandatory(requirement1_activity)
    if requirement2:
        requirement2_activity = next(a for a in activities if a['number'] == requirement2)
        requirement2_activity['mandatory'] = 1
        convert_requirements_to_mandatory(requirement2_activity)

mandatory_activities = [activity for activity in activities if activity['mandatory'] == 1]
new_mandatory_activities = []
for activity in mandatory_activities:
    if activity['requirement1']:
        new_mandatory_activities.append(activity['requirement1'])
        convert_requirements_to_mandatory(activity)
    if activity['requirement2']:
        new_mandatory_activities.append(activity['requirement2'])
        convert_requirements_to_mandatory(activity)

subtopics = {}  # Dictionary to store the sorted subtopics
for i in range(1, 9):
    subtopic = [activity for activity in activities if activity['subtopic'] == i]

    for activity in subtopic:
        x = activity['value'] / activity['duration']
        activity['Val / Dur'] = round(x, 3)
    sorted_subtopic = sorted(subtopic, key=lambda x: (-x['mandatory'], -x['Val / Dur']))
    subtopics[f'Subtopic {i}'] = sorted_subtopic

for subtopic_name, subtopic in subtopics.items():
    sum_values = 0
    sum_duration = 0
    sequence_subtopic = []
    fin_sum_values = 0
    fin_dur_values = 0

    index = 0
    while sum_values < Kmin and index < len(subtopic):
        activity = subtopic[index]
        sum_values += activity['value']
        sum_duration += activity['duration']
        sequence_subtopic.append(activity['number'])
        fin_sum_values = sum_values
        fin_dur_values = sum_duration
        index += 1

    # Check if the loop terminated due to reaching Kmin or end of the list
    if sum_values >= Kmax:
        sequence_subtopic.pop()  # Remove the last added activity

    print(f"Subtopic: {subtopic_name}")
    print("Sequence:", sequence_subtopic)
    print("Total Value:", fin_sum_values)
    print("Total Duration:", fin_dur_values)
    print()