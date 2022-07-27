"""CSV_Modifier

This script allows the user to bring raw data to experiment 1 from:
"Preferred mental models in reasoning about spatial relations", by

GEORG JAHN
Chemnitz University of Technology, Chemnitz, Germany

MARKUS KNAUFF
Giessen University, Giessen, Germany

P. N. JOHNSON-LAIRD
Princeton University, Princeton, New Jersey

into a form to use for evaluation with CCOBRA (https://github.com/CognitiveComputationLab/ccobra).
# TODO describe in more detail.
"""

import csv

Modification = {
    'trial111': ['between;B;C;D/right;A;C/next;B;C', 'N'],
    'trial112': ['between;B;C;D/right;A;C/next;A;D', 'F'],
    'trial113': ['between;B;C;D/right;A;C/next;A;B', 'R'],
    'trial114': ['between;B;C;D/right;A;C/next;B;D', 'I'],
    'trial121': ['between;B;C;D/right;A;C/next;C;D', 'N'],
    'trial122': ['between;B;C;D/right;A;C/next;D;A', 'R'],
    'trial123': ['between;B;C;D/right;A;C/next;B;A', 'F'],
    'trial124': ['between;B;C;D/right;A;C/next;B;D', 'I'],
    'trial131': ['between;B;C;D/left;A;C/next;C;A', 'N'],
    'trial132': ['between;B;C;D/left;A;C/next;B;A', 'F'],
    'trial133': ['between;B;C;D/left;A;C/next;D;A', 'R'],
    'trial134': ['between;B;C;D/left;A;C/next;B;D', 'I'],
    'trial141': ['between;B;C;D/left;C;A/next;B;C', 'N'],
    'trial142': ['between;B;C;D/left;C;A/next;A;B', 'R'],
    'trial143': ['between;B;C;D/left;C;A/next;A;D', 'F'],
    'trial144': ['between;B;C;D/left;C;A/next;B;D', 'I'],
    'trial211': ['between;B;C;D/right;A;D/next;B;C', 'N'],
    'trial212': ['between;B;C;D/right;A;D/next;C;D', 'N'],
    'trial213': ['between;B;C;D/right;A;D/next;A;C', 'R'],
    'trial214': ['between;B;C;D/right;A;D/next;B;D', 'I'],
    'trial221': ['between;B;C;D/right;D;A/next;B;C', 'N'],
    'trial222': ['between;B;C;D/right;D;A/next;D;C', 'F'],
    'trial223': ['between;B;C;D/right;D;A/next;C;A', 'F'],
    'trial224': ['between;B;C;D/right;D;A/next;B;D', 'I'],
    'trial231': ['between;B;C;D/left;A;B/next;C;D', 'N'],
    'trial232': ['between;B;C;D/left;A;B/next;B;C', 'N'],
    'trial233': ['between;B;C;D/left;A;B/next;C;A', 'R'],
    'trial234': ['between;B;C;D/left;A;B/next;B;D', 'I'],
    'trial241': ['between;B;C;D/left;B;A/next;C;D', 'N'],
    'trial242': ['between;B;C;D/left;B;A/next;C;B', 'F'],
    'trial243': ['between;B;C;D/left;B;A/next;A;C', 'F'],
    'trial244': ['between;B;C;D/left;B;A/next;B;D', 'I'],
    'trial311': ['next;A;B/between;B;C;D/next;C;D', 'N'],
    'trial312': ['next;A;B/between;B;C;D/left;D;B', 'R'],
    'trial313': ['next;A;B/between;B;C;D/left;D;A', 'R'],
    'trial314': ['next;A;B/between;B;C;D/next;A;D', 'I'],
    'trial321': ['next;B;A/between;B;C;D/next;C;D', 'N'],
    'trial322': ['next;B;A/between;B;C;D/left;D;B', 'R'],
    'trial323': ['next;B;A/between;B;C;D/left;D;A', 'R'],
    'trial324': ['next;B;A/between;B;C;D/next;A;D', 'I'],
    'trial331': ['between;B;C;D/next;D;A/next;B;C', 'N'],
    'trial332': ['between;B;C;D/next;D;A/left;D;B', 'R'],
    'trial333': ['between;B;C;D/next;D;A/left;A;B', 'R'],
    'trial334': ['between;B;C;D/next;D;A/next;B;A', 'I'],
    'trial341': ['between;B;C;D/next;A;D/next;B;C', 'N'],
    'trial342': ['between;B;C;D/next;A;D/left;D;B', 'R'],
    'trial343': ['between;B;C;D/next;A;D/left;A;B', 'R'],
    'trial344': ['between;B;C;D/next;A;D/next;B;A', 'I'],
             }


def extract_information():
    """Extracts information from raw dataset to be processed in prepare data and written in new csv file in write_csv.

    Returns
    -------
    data : list()
        List of various data types containing all raw or expanded information form raw data.
    """
    data = []
    count = 0
    with open('data_raw_full.csv', 'r', encoding='utf-8-sig', newline='') as csvfile:
        reader = csv.reader(csvfile)
        # skip header
        next(reader, None)
        for row in reader:
            # process each row
            identifier = row[0]
            sequence = count % 48
            task_id = row[1]
            task = Modification[task_id][0]
            task_type = Modification[task_id][1]
            consistent = determine_consistency(row[1])
            reaction_time = row[2]
            error = convert_to_true_false(row[3])
            response = determine_response(consistent, error)
            errordr = convert_to_true_false(row[4])
            count += 1
            # Keep in mind! Right now response encoding is as follows:
            # consistent = str(True) | str(False)
            # task == consistent & error == False / 0 (original dataset) => True [Participant drew correct MM for consistent task]
            # task == consistent & error == True / 1 (original dataset) => None [Participant made a mistake to predict concistent task (either wrong MM or not recocnising that task is concistent]
            # task == inconsistent & error == False / 0 (original dataset) => None [Participant predicted inconsistancy correct -> drew NO MM]
            # !!!task == inconsistent & error == False / 1 (original dataset) => Some random MM (NO WAY OF KNOWING) [Participant drew a MM for inconcistent task]

            # find out all problematic cases.
            # if consistent == 'False' and error == 'True':
            #     print('Id: {}\nTask_id: {}\ntask: {}\nsequence: {}\n'.format(identifier, task_id, task, sequence))
            row_data = prepare_data(identifier, sequence, task_id, task_type, task,
                                    response, consistent, reaction_time, error, errordr)
            data.append(row_data)
    return data


def prepare_data(identifier, sequence, task_id, task_type, task,
                 response, consistent, reaction_time, error, errordr):
    """Function to order data for clarity. No other functionality.

    Parameters
    ----------
    identifier : int
        Participant id.
    sequence : int
        Order of presented tasks.
    task_id : str
        Identifier for tasks e.g. 'trial231'.
    task_type : str
        Type of task in original experiment (N = neutral, R=reordering, F=filler, I=inconsistent).
    task : list(str)
        Task description.
    response : list(str)
        Response given to presented task by participant.
    consistent : bool
        True if task has other solution than None, false otherwise.
    reaction_time : int
        Time participant took to solve task.
    error : bool
        True if participant did not solve task fully correct, false otherwise.
    errordr : bool
        Unknown, from raw data.

    Returns
    -------
    data : list()
        List of various data types containing all raw or expanded information form raw data.
    """
    data = list()
    data.append(identifier)
    data.append(sequence)
    data.append('spatial')
    data.append(task_id)
    data.append(task_type)
    data.append(task)
    data.append('free_response')
    data.append(response)
    data.append('free_verify')
    data.append(consistent)
    data.append(reaction_time)
    data.append(error)
    data.append(errordr)
    return data


def write_csv(data):
    """Writes data to new csv file.

    Parameters
    ----------
    data : list()
        List of various data types containing all raw or expanded information form raw data.
    """
    header = ['id', 'sequence', 'domain', 'task_id', 'task_type', 'task',
              'response_type', 'response', 'choices', 'consistent', 'reaction_time', 'error', 'errordr']

    with open('Jahn2007_experiment_1.csv', 'w', newline='') as newfile:
        writer = csv.writer(newfile)
        writer.writerow(header)
        writer.writerows(data)


def convert_to_true_false(string):
    """Change 1/0 to True/False, because some csv reader present data nicer that way....
    """
    # Just for my CSV viewer
    if string == '1':
        return 'True'
    else:
        return 'False'


def determine_consistency(task_id):
    """Determine if task is consistent.

    Consistent have a solution / solutions except None. Inconsistent task only solution None.
    All tasks with 4 as last number in der id are inconsistent.

    Parameters
    ----------
    task_id : str
        Identifier for tasks e.g. 'trial231'.
    Returns
    -------
    bool
        True if there is a solution except None, false otherwise.
    """
    if task_id[-1] == '4':
        return 'False'
    else:
        return 'True'


def determine_response(consistent, error):
    """Calculate response of participant from other available information included in raw data.

    Parameters
    ----------
    consistent : bool
        True if task has other solution than None, false otherwise.
    error : bool
        True if participant did not solve task fully correct, false otherwise.
    Returns
    -------
    response : str
        Response participant gave to a specific task.
    """
    if consistent == 'True' and error == 'False':
        response = 'True'
    elif consistent == 'False' and error == 'True':
        response = 'Unknown'
    else:
        response = 'None'
    return response


def main():
    data = extract_information()
    write_csv(data)


if __name__ == "__main__":
    main()
