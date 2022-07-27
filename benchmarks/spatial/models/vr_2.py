import ccobra
from VerbalReasonerHelpers import Encoder
from VerbalReasonerHelpers import SolutionSets
from VerbalReasonerHelpers import Queue

# choose encoding the model is evaluated on
Encoding = 2
AlternativeSolution = False


class VerbalReasoningModel(ccobra.CCobraModel):
    def __init__(self, name='vr_2'):
        super(VerbalReasoningModel, self).__init__(name, ['spatial'], ['free_response'])

    @staticmethod
    def predict_free_response(queue, last_premise, solution_set):
        mm = queue.readout_mm()
        prediction = 'None'
        if queue.validate_premise(last_premise):
            prediction = Encoder.encode_response(mm, solution_set)
        return prediction

    def predict(self, item, **kwargs):
        enc_task = Encoder.encode_between(item.task, Encoding)
        queue = Queue.Queue('->')
        queue.build_queue(enc_task)
        if AlternativeSolution:
            solution_set = SolutionSets.AlternativeSolutions[kwargs['task_id']]
        else:
            solution_set = SolutionSets.Solutions[kwargs['task_id']]
        return self.predict_free_response(queue, enc_task[-1], solution_set)
