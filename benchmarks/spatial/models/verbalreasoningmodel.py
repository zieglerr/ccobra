import ccobra
from VerbalReasonerHelpers import Encoder
from VerbalReasonerHelpers import SolutionSets
from VerbalReasonerHelpers import Queue

# choose encoding the model is evaluated on
Encoding_1 = 1  # BCD or CBD
Encoding_2 = 2  # BCD
Encoding_3 = 3  # DCB
Encoding_4 = 4  # DCB or CBD
Encoding_5 = 5  #
Encoding_6 = 6  #
Encoding_7 = 7  #
Encoding_8 = 8  #
AlternativeSolution = True


class VerbalReasoningModel(ccobra.CCobraModel):
    def __init__(self, name='model_0'):
        super(VerbalReasoningModel, self).__init__(name, ['spatial'], ['free_response'])
        print('_________START____________')
        self.tmp_counter = 0

    @staticmethod
    def predict_free_response(queue, last_premise, solution_set):
        mm = queue.readout_mm()
        # default predict
        prediction = 'None'
        # check if all 3 premises are combinable.
        if queue.validate_premise(last_premise):
            # encode task form explicit mm to binary response.
            prediction = Encoder.encode_response(mm, solution_set)
        return prediction

    def predict(self, item, **kwargs):
        # print('__________________PREDICT___________________')
        # print('Participant_ID: {} || Task_ID: {}'.format(item.identifier, kwargs['task_id']))
        enc_task = Encoder.encode_between(item.task, Encoding_2)
        queue = Queue.Queue('->')
        queue.build_queue(enc_task)
        tmp_enc_task = Encoder.encode_between(item.task, Encoding_3)  # TODO remove
        if AlternativeSolution:
            solution_set = SolutionSets.AlternativeSolutions[kwargs['task_id']]
        else:
            solution_set = SolutionSets.Solutions[kwargs['task_id']]
        # TODO remove
        # mm = queue.readout_mm()
        # print('Participant_ID: {} || Task_ID: {}'.format(item.identifier, kwargs['task_id']))
        # print('Encoded_task: {} \nMental-Model: {}  \nLast_Premise: {} \nSolution_Set: {} \nModel_Prediction: {}'
        #           .format(enc_task, mm, enc_task[-1], solution_set, prediction))
        # tmp_enc_task = Encoder.encode_between(item.task, 3)
        # tmp_queue = Queue.Queue('->')
        # tmp_queue.build_queue(tmp_enc_task)
        # mm_2 = queue.readout_mm()
        # mm_3 = tmp_queue.readout_mm()
        # prediction_2 = self.predict_free_response(queue, enc_task[-1], solution_set)
        # prediction_3 = self.predict_free_response(tmp_queue, tmp_enc_task[-1], solution_set)
        # if kwargs['task_type'] == 'N':
        #     if prediction_3 == 'True':
        #         print('Task_ID = {} \n mm3 = {}'.format(kwargs['task_id'], mm_3))
        #         self.tmp_counter += 1
        #     elif prediction_3 == 'None':
        #         self.tmp_counter -= 1
        # # print(self.tmp_counter)
        #     # print('Model DCB prediction: {} \n Model BCD prediction: {}'.format(prediction_3, prediction_2))
        # if prediction_2 != prediction_3:
        #     return 1
        #     print('task_id: {} \n task: {}  \ntask_type: {} \nenc2: {}  |||| enc3: {}\n mm2: {} ||||| mm3: {}'
        #           .format(kwargs['task_id'], item.task, kwargs['task_type'], tmp_enc_task, enc_task, mm_2, mm_3))
        return self.predict_free_response(queue, enc_task[-1], solution_set)
