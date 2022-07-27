import copy


class QueueItem:
    """A single item of the mental queue constructed by verbal reasoning model.

    Attributes
    ----------
    data : str
        The object data contained by the queue item.
    next : object
        Pointer to the next item in the mental queue.
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
    """The mental queue constructed by verbal reasoning model.

    Attributes
    ----------
    preferred_direction : str
        The implicit direction of the queue.
    first : object
        The currently first object in the queue.
    """

    def __init__(self, preferred_direction):
        """Initialize the queue.

        Parameters
        ----------
        preferred_direction : str
            The implicit direction of the queue.
        """
        self.direction = preferred_direction
        self.first = None

    def build_queue(self, task):
        """Creates a mental queue from task.

        A task contains multiple premises. A premises includes two objects connected by a spatial relation.

        Parameters
        ----------
        task : list(str)
            Task description.
        """
        first_premise = task[0]
        end = len(task) - 1
        self.insert_first_premise(first_premise)
        for i in range(1, end):
            self.insert(task[i])

    def find_reference_object(self, premise):
        """Searches for object(reference) already in mental queue.

        Only implemented for the case that exactly one object is in queue and the other object from the premise is not.

        Parameters
        ----------
        premise : list(str)
            Premise encoded as list of strings e.g. ['left', 'A', 'B'] resembles "A left of B".

        Returns
        -------
        current.data : str
            Data held by QueueItem object.

        Raises
        ------
        NotImplementedError
            If no object from premise is already included in mental queue.
        """
        current = self.first
        while True:
            if current.data == premise[1]:
                return current.data
            elif current.data == premise[2]:
                return current.data
            if current.next is None:
                break
            else:
                current = current.next
        raise NotImplementedError("No reference object found in queue.")

    @staticmethod
    def inverse_premise(premise):
        """Inverse a premise logically equivalent.

        E.g. "A left of B" inverse is "B right of A"

        Parameters
        ----------
        premise : list(str)
            Premise encoded as list of strings e.g. ['left', 'A', 'B'] resembles "A left of B".

        Returns
        -------
        inv_premise : list(str)
            Inverse from parameter premise.
        """
        inv_premise = copy.deepcopy(premise)
        if premise[0] == 'left':
            inv_premise[0], inv_premise[1], inv_premise[2] = 'right', inv_premise[2], inv_premise[1]
        elif premise[0] == 'right':
            inv_premise[0], inv_premise[1], inv_premise[2] = 'left', inv_premise[2], inv_premise[1]
        else:
            inv_premise[1], inv_premise[2] = inv_premise[2], inv_premise[1]
        return inv_premise

    def insert(self, premise):
        """Insert new premise into mental queue.

        Parameters
        ----------
        premise : list(str)
            Premise encoded as list of strings e.g. ['left', 'A', 'B'] resembles "A left of B".

        Raises
        ------
        NotImplementedError
            If implicit direction of queue is set to: From right to left.
        """
        tmp_premise = copy.deepcopy(premise)
        # make sure new object not in queue is at last position of premise.
        if self.find_reference_object(premise) == premise[2]:
            tmp_premise = self.inverse_premise(premise)
        if self.direction == '->':
            if tmp_premise[0] == 'left':
                self.insert_end(tmp_premise[2])
            elif tmp_premise[0] == 'right':
                self.insert_directly_before(tmp_premise[1], tmp_premise[2])
            elif premise[0] == 'next':
                self.insert_directly_after(tmp_premise[1], tmp_premise[2])
        elif self.direction == '<-':
            raise NotImplementedError('Implicit direction: From right to left')

    def insert_end(self, target):
        """Inserts premise at the end of the mental queue.

        Parameters
        ----------
        target : str
           Target object added to queue.
        """
        current = self.first
        while current.next is not None:
            current = current.next
        current.next = QueueItem(target)

    def insert_directly_before(self, reference, target):
        """Inserts target directly before reference object in mental queue.

        Parameters
        ----------
        reference : str
            References object already included in queue.
        target : str
            Target object added to queue.
        """
        current = self.first
        previous = None
        while True:
            if current.data == reference:
                new_item = QueueItem(target)
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

    def insert_directly_after(self, reference, target):
        """Inserts target object directly after reference object in mental queue.

        Parameters
        ----------
        reference : str
            References object already included in queue.
        target : str
            Target object added to queue.
        """
        current = self.first
        while True:
            if current.data == reference:
                new_item = QueueItem(target)
                new_item.next = current.next
                current.next = new_item
            if current.next is None:
                break
            else:
                current = current.next

    def insert_first_premise(self, premise):
        """Inserts first two objects from first task premise to mental queue.

        Parameters
        ----------
        premise : list(str)
            Premise encoded as list of strings e.g. ['left', 'A', 'B'] resembles "A left of B".

        Raises
        ------
        NotImplementedError
            If implicit direction of queue is set to: From right to left.
        """
        if self.direction == '->':
            if premise[0] == 'left' or premise[0] == 'next':
                self.first = QueueItem(premise[1])
                self.first.next = QueueItem(premise[2])
            else:
                self.first = QueueItem(premise[2])
                self.first.next = QueueItem(premise[1])
        elif self.direction == '<-':
            raise NotImplementedError('Implicit direction: From right to left')

    def validate_premise(self, premise):
        """Checks if premise is valid in current mental queue.

        Parameters
        ----------
        premise : str
            Premise to be validated.

        Returns
        -------
        bool
            True if premise is true in current mental queue, false otherwise.

        Raises
        ------
        NotImplementedError
            If implicit direction of queue is set to: From right to left.
        """
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
        first_object = self.find_reference_object(premise)
        if self.direction == '->' and first_object == premise[1]:
            if premise[0] == 'left':
                return True
        elif self.direction == '->' and first_object == premise[2]:
            if premise[0] == 'right':
                return True
        elif self.direction == '<-':
            raise NotImplementedError('Implicit direction: From right to left')
        return False

    def readout_mm(self):
        """Reads out mental model from mental queue.

        Returns
        -------
        mental_model : list(str)
            Representation of mental model held by mental queue.
        """
        mental_model = []
        current = self.first
        while True:
            mental_model.append(current.data)
            if current.next is None:
                break
            else:
                current = current.next
        return mental_model
