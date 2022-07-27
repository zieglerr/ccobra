import ccobra
import copy
from VerbalReasonerHelpers import Encoder

Solutions = {
    'trial_test': [None],
    'trial111': [['B', 'C', 'A', 'D'], ['B', 'C', 'D', 'A'], ['D', 'C', 'B', 'A']],
    'trial112': [['B', 'C', 'A', 'D'], ['B', 'C', 'D', 'A']],
    'trial113': [['D', 'C', 'A', 'B'], ['D', 'C', 'B', 'A']],
    'trial114': [None],
    'trial121': [['B', 'A', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'D', 'C', 'B']],
    'trial122': [['D', 'A', 'C', 'B'], ['A', 'D', 'C', 'B']],
    'trial123': [['B', 'A', 'C', 'D'], ['A', 'B', 'C', 'D']],
    'trial124': [None],
    'trial131': [['B', 'A', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'D', 'C', 'B']],
    'trial132': [['B', 'A', 'C', 'D'], ['A', 'B', 'C', 'D']],
    'trial133': [['D', 'A', 'C', 'B'], ['A', 'D', 'C', 'B']],
    'trial134': [None],
    'trial141': [['B', 'C', 'A', 'D'], ['B', 'C', 'D', 'A'], ['D', 'C', 'B', 'A']],
    'trial142': [['D', 'C', 'A', 'B'], ['D', 'C', 'B', 'A']],
    'trial143': [['B', 'C', 'A', 'D'], ['B', 'C', 'D', 'A']],
    'trial144': [None],

    'trial211': [['B', 'C', 'D', 'A'], ['D', 'A', 'C', 'B'], ['D', 'C', 'B', 'A']],
    'trial212': [['B', 'C', 'D', 'A'], ['D', 'C', 'A', 'B'], ['D', 'C', 'B', 'A']],
    'trial213': [['D', 'A', 'C', 'B'], ['D', 'C', 'A', 'B']],
    'trial214': [None],
    'trial221': [['B', 'C', 'A', 'D'], ['A', 'D', 'C', 'B'], ['A', 'B', 'C', 'D']],
    'trial222': [['A', 'D', 'C', 'B'], ['B', 'A', 'C', 'D'], ['A', 'B', 'C', 'D']],
    'trial223': [['B', 'C', 'A', 'D'], ['B', 'A', 'C', 'D']],
    'trial224': [None],
    'trial231': [['A', 'B', 'C', 'D'], ['D', 'C', 'A', 'B'], ['A', 'D', 'C', 'B']],
    'trial232': [['A', 'B', 'C', 'D'], ['D', 'A', 'C', 'B'], ['A', 'D', 'C', 'B']],
    'trial233': [['D', 'C', 'A', 'B'], ['D', 'A', 'C', 'B']],
    'trial234': [None],
    'trial241': [['B', 'A', 'C', 'D'], ['D', 'C', 'B', 'A'], ['B', 'C', 'D', 'A']],
    'trial242': [['D', 'C', 'B', 'A'], ['B', 'C', 'A', 'D'], ['B', 'C', 'D', 'A']],
    'trial243': [['B', 'A', 'C', 'D'], ['B', 'C', 'A', 'D']],
    'trial244': [None],

    'trial311': [['A', 'B', 'C', 'D'], ['B', 'A', 'C', 'D'], ['D', 'C', 'A', 'B'], ['D', 'C', 'B', 'A']],
    'trial312': [['D', 'C', 'A', 'B'], ['D', 'C', 'B', 'A']],
    'trial313': [['D', 'C', 'A', 'B'], ['D', 'C', 'B', 'A']],
    'trial314': [None],
    'trial321': [['A', 'B', 'C', 'D'], ['B', 'A', 'C', 'D'], ['D', 'C', 'A', 'B'], ['D', 'C', 'B', 'A']],
    'trial322': [['D', 'C', 'A', 'B'], ['D', 'C', 'B', 'A']],
    'trial323': [['D', 'C', 'A', 'B'], ['D', 'C', 'B', 'A']],
    'trial324': [None],
    'trial331': [['B', 'C', 'D', 'A'], ['B', 'C', 'A', 'D'], ['D', 'A', 'C', 'B'], ['A', 'D', 'C', 'B']],
    'trial332': [['D', 'A', 'C', 'B'], ['A', 'D', 'C', 'B']],
    'trial333': [['D', 'A', 'C', 'B'], ['A', 'D', 'C', 'B']],
    'trial334': [None],
    'trial341': [['B', 'C', 'D', 'A'], ['B', 'C', 'A', 'D'], ['D', 'A', 'C', 'B'], ['A', 'D', 'C', 'B']],
    'trial342': [['D', 'A', 'C', 'B'], ['A', 'D', 'C', 'B']],
    'trial343': [['D', 'A', 'C', 'B'], ['A', 'D', 'C', 'B']],
    'trial344': [None],
             }

AlternativeSolutions = {
    'trial_test': [None],
    'trial111': [['B', 'C', 'A', 'D'], ['B', 'C', 'D', 'A']],
    'trial112': [['B', 'C', 'A', 'D'], ['B', 'C', 'D', 'A']],
    'trial113': [['D', 'C', 'A', 'B'], ['D', 'C', 'B', 'A']],
    'trial114': [None],
    'trial121': [['B', 'A', 'C', 'D'], ['A', 'B', 'C', 'D']],
    'trial122': [['D', 'A', 'C', 'B'], ['A', 'D', 'C', 'B']],
    'trial123': [['B', 'A', 'C', 'D'], ['A', 'B', 'C', 'D']],
    'trial124': [None],
    'trial131': [['B', 'A', 'C', 'D'], ['A', 'B', 'C', 'D']],
    'trial132': [['B', 'A', 'C', 'D'], ['A', 'B', 'C', 'D']],
    'trial133': [['D', 'A', 'C', 'B'], ['A', 'D', 'C', 'B']],
    'trial134': [None],
    'trial141': [['B', 'C', 'A', 'D'], ['B', 'C', 'D', 'A']],
    'trial142': [['D', 'C', 'A', 'B'], ['D', 'C', 'B', 'A']],
    'trial143': [['B', 'C', 'A', 'D'], ['B', 'C', 'D', 'A']],
    'trial144': [None],

    'trial211': [['B', 'C', 'D', 'A']],
    'trial212': [['B', 'C', 'D', 'A']],
    'trial213': [['D', 'A', 'C', 'B'], ['D', 'C', 'A', 'B']],
    'trial214': [None],
    'trial221': [['B', 'C', 'A', 'D'], ['A', 'B', 'C', 'D']],
    'trial222': [['A', 'D', 'C', 'B'], ['B', 'A', 'C', 'D'], ['A', 'B', 'C', 'D']],
    'trial223': [['B', 'C', 'A', 'D'], ['B', 'A', 'C', 'D']],
    'trial224': [None],
    'trial231': [['A', 'B', 'C', 'D']],
    'trial232': [['A', 'B', 'C', 'D']],
    'trial233': [['D', 'C', 'A', 'B'], ['D', 'A', 'C', 'B']],
    'trial234': [None],
    'trial241': [['B', 'A', 'C', 'D'], ['B', 'C', 'D', 'A']],
    'trial242': [['D', 'C', 'B', 'A'], ['B', 'C', 'A', 'D'], ['B', 'C', 'D', 'A']],
    'trial243': [['B', 'A', 'C', 'D'], ['B', 'C', 'A', 'D']],
    'trial244': [None],

    'trial311': [['A', 'B', 'C', 'D'], ['B', 'A', 'C', 'D']],
    'trial312': [['D', 'C', 'A', 'B'], ['D', 'C', 'B', 'A']],
    'trial313': [['D', 'C', 'A', 'B'], ['D', 'C', 'B', 'A']],
    'trial314': [None],
    'trial321': [['A', 'B', 'C', 'D'], ['B', 'A', 'C', 'D']],
    'trial322': [['D', 'C', 'A', 'B'], ['D', 'C', 'B', 'A']],
    'trial323': [['D', 'C', 'A', 'B'], ['D', 'C', 'B', 'A']],
    'trial324': [None],
    'trial331': [['B', 'C', 'D', 'A'], ['B', 'C', 'A', 'D']],
    'trial332': [['D', 'A', 'C', 'B'], ['A', 'D', 'C', 'B']],
    'trial333': [['D', 'A', 'C', 'B'], ['A', 'D', 'C', 'B']],
    'trial334': [None],
    'trial341': [['B', 'C', 'D', 'A'], ['B', 'C', 'A', 'D']],
    'trial342': [['D', 'A', 'C', 'B'], ['A', 'D', 'C', 'B']],
    'trial343': [['D', 'A', 'C', 'B'], ['A', 'D', 'C', 'B']],
    'trial344': [None],
             }


# class Participant:
#     def __init__(self, identifier):
#         """ Initialize the item.
#         Parameters
#         ----------
#         identifier : str
#             The object data contained by the queue item.
#         """
#         self.id = identifier
#         self.direction = None
#
#     def set_direction(self, left_to_right_count, right_to_left_count):
#         if right_to_left_count > left_to_right_count:
#             self.direction = "<-"
#         else:
#             self.direction = "->"


class QueueItem:
    """ A single item of the mental queue constructed by the virtual reasoner.
    """

    def __init__(self, data):
        """ Initialize the item.
        Parameters
        ----------
        data : str
            The object data contained by the queue item.
        """
        self.data = data
        self.next = None


class Queue:
    """ The mental queue constructed by the virtual reasoner.
    """

    def __init__(self, preferred_direction):
        """ Initialize the queue.
        Parameters
        ----------
        preferred_direction : intDTF
            Specify whether one- or two-dimensional queue should be
            constructed.
        """
        self.direction = preferred_direction
        self.first = None

    def build_queue(self, task):
        first_premise = task[0]
        end = len(task) - 1
        self.insert_first_premise(first_premise)
        for i in range(1, end):
            self.insert(task[i], self.direction)
        return

    def find_first(self, premise):
        current = self.first
        while True:
            if current.data == premise[1]:
                return current
            elif current.data == premise[2]:
                return current
            if current.next is None:
                break
            else:
                current = current.next

    @staticmethod
    def inverse_premise(premise):
        inv_premise = copy.deepcopy(premise)
        if premise[0] == 'left':
            inv_premise[0], inv_premise[1], inv_premise[2] = 'right', inv_premise[2], inv_premise[1]
        elif premise[0] == 'right':
            inv_premise[0], inv_premise[1], inv_premise[2] = 'left', inv_premise[2], inv_premise[1]
        else:
            inv_premise[1], inv_premise[2] = inv_premise[2], inv_premise[1]
        return inv_premise

    def insert(self, premise, direction):
        tmp_premise = copy.deepcopy(premise)
        if self.find_first(premise).data == premise[2]:
            tmp_premise = self.inverse_premise(premise)
        if direction == '->':
            if tmp_premise[0] == 'left':
                self.insert_end(tmp_premise)
            elif tmp_premise[0] == 'right':
                self.insert_directly_before(tmp_premise)
            elif premise[0] == 'next':
                self.insert_directly_after(tmp_premise)
        # TODO add if both directions are implemented
        elif direction == '<-':
            print('HOW DID I END HEAR in INSERT')

    def insert_end(self, premise):
        current = self.first
        while current.next is not None:
            current = current.next
        current.next = QueueItem(premise[2])

    def insert_directly_before(self, premise):
        current = self.first
        previous = None
        while True:
            if current.data == premise[1]:
                new_item = QueueItem(premise[2])
                if previous is None:
                    new_item.next = self.first
                    self.first = new_item
                else:
                    new_item.next = current
                    previous.next = new_item
            if current.next is None:
                break
            else:
                previous = current
                current = current.next

    def insert_directly_after(self, premise):
        current = self.first
        while True:
            if current.data == premise[1]:
                new_item = QueueItem(premise[2])
                new_item.next = current.next
                current.next = new_item
            if current.next is None:
                break
            else:
                current = current.next

    def insert_first_premise(self, premise):
        if self.direction == '->':
            if premise[0] == 'left' or premise[0] == 'next':
                self.first = QueueItem(premise[1])
                self.first.next = QueueItem(premise[2])
            else:
                self.first = QueueItem(premise[2])
                self.first.next = QueueItem(premise[1])
        # TODO add if both direction are implemented
        # elif self.direction = '<-':
        else:
            print('SOMETHING WENT TERRIBLY WRONG in insight first')

    def validate_premise(self, premise):
        if premise[0] == 'next':
            current = self.first
            while True:
                if current.data == premise[1] or current.data == premise[2]:
                    current = current.next
                    if current.data == premise[1] or current.data == premise[2]:
                        return True
                    else:
                        return False
                if current.next is None:
                    break
                else:
                    current = current.next
        first_object = self.find_first(premise)
        if self.direction == '->' and first_object.data == premise[1]:
            if premise[0] == 'left':
                return True
        elif self.direction == '->' and first_object.data == premise[2]:
            if premise[0] == 'right':
                return True
        # TODO add if both directions are implemented.
        elif self.direction == '<-':
            print('LOOK AT VALIDATE PREMISE')
        return False

    def readout_mm(self):
        mental_model = []
        current = self.first
        while True:
            mental_model.append(current.data)
            if current.next is None:
                break
            else:
                current = current.next
        return mental_model

    def print(self):
        # USE readout instead
        q = list()
        q.append(self.direction)
        current = self.first
        while True:
            q.append(current.data)
            if current.next is None:
                break
            else:
                current = current.next
        print(q)


class VerbalReasoningModel(ccobra.CCobraModel):
    def __init__(self, name='model_0'):
        super(VerbalReasoningModel, self).__init__(name, ['spatial'], ['free_response'])
        print('_________START____________')

    @staticmethod
    def encode_task(task, encoding_type=4):
        """ Encode relation between to be represented with left and right.
        ----------
        task : list
            Task to produce a response for.
        """
        # print('Type =', encoding_type)
        enc_task = []
        for premise in task:
            if premise[0] == 'between':
                if encoding_type == 1:
                    # BCD or CBD
                    # between;B,C,D to:
                    # 1 left;B;D
                    # 2 left;C,D
                    premise1 = ['left', premise[1], premise[3]]
                    premise2 = ['left', premise[2], premise[3]]
                elif encoding_type == 2:
                    # BCD
                    # between;B,C,D to
                    # 1 left;B;C
                    # 2 left;C;D
                    premise1 = ['left', premise[1], premise[2]]
                    premise2 = ['left', premise[2], premise[3]]
                elif encoding_type == 3:
                    # DCB
                    # between;B,C,D to
                    # 1 left;C;B
                    # 2 left;D;C
                    premise1 = ['left', premise[1], premise[2]]
                    premise2 = ['left', premise[3], premise[2]]
                elif encoding_type == 4:
                    # DCB or CBD
                    # between;B,C,D to:
                    # 1 left;D;B
                    # 2 left;C,B
                    premise1 = ['left', premise[3], premise[1]]
                    premise2 = ['left', premise[2], premise[1]]
                enc_task.append(premise1)
                enc_task.append(premise2)
            else:
                enc_task.append(premise)
        return enc_task

    @staticmethod
    def get_prediction(queue, last_premise, solution_set):
        mm = queue.readout_mm()
        # default predict
        prediction = 'None'
        # check if all 3 premises are combinable.
        if queue.validate_premise(last_premise):
            # encode explicit mm prediction from model to expected known answer of participant.
            # 'None' resembles the situation, where the participant does not expect that the task is solvable.
            if mm in solution_set:
                prediction = 'True'
            else:
                prediction = 'None'
        return prediction

    def predict(self, item, **kwargs):
        # print('__________________PREDICT___________________')
        # TODO better way for evaluation between different encodings, solution_sets and later models.
        enc_task = self.encode_task(item.task, 4)
        # solution_set = AlternativeSolutions[kwargs['task_id']]
        solution_set = Solutions[kwargs['task_id']]
        queue = Queue('->')
        queue.build_queue(enc_task)
        prediction = self.get_prediction(queue, enc_task[-1], solution_set)
        # mm = queue.readout_mm()
        # print('Participant_ID: {} || Task_ID: {}'.format(item.identifier, kwargs['task_id']))

        # print('Encoded_task: {} \nMental-Model: {}  \nLast_Premise: {} \nSolution_Set: {} \nModel_Prediction: {}'
        #           .format(enc_task, mm, enc_task[-1], solution_set, prediction))
        return prediction
