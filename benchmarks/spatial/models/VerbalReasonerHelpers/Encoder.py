def encode_between(task, encoding):
    """ Encode relation between to be represented with relations left and right in a task.

    A task contains multiple premises. A premises includes multiple objects connected by a spatial relation.
    Encoding example: [between;B;C;D] becomes 1) [left;B;C] and 2) [left;C,D].

    Parameters
    ----------
    task : list(str)
        Task description.
    encoding : int
        Integer representing the type of encoding chosen.

    Returns
    ----------
    enc_task : list(str)
        Encoded task description.
    """
    enc_task = []
    for premise in task:
        if premise[0] == 'between':
            if encoding == 1:
                # BCD or CBD
                # between;B,C,D to:
                # 1 left;B;D
                # 2 left;C,D
                premise1 = ['left', premise[1], premise[3]]
                premise2 = ['left', premise[2], premise[3]]
            elif encoding == 2:
                # BCD
                # between;B,C,D to
                # 1 left;B;C
                # 2 left;C;D
                premise1 = ['left', premise[1], premise[2]]
                premise2 = ['left', premise[2], premise[3]]
            elif encoding == 3:
                # DCB
                # between;B,C,D to
                # 1 left;C;B
                # 2 left;D;C
                premise1 = ['left', premise[2], premise[1]]
                premise2 = ['left', premise[3], premise[2]]
            elif encoding == 4:
                # DCB or CBD
                # between;B,C,D to:
                # 1 left;D;B
                # 2 left;C,B
                premise1 = ['left', premise[3], premise[1]]
                premise2 = ['left', premise[2], premise[1]]
            elif encoding == 5:
                # BCD with right
                # between;B;C;D to:
                # 1 right;C;B
                # 2 right;D;C
                premise1 = ['right', premise[2], premise[1]]
                premise2 = ['right', premise[3], premise[2]]
            elif encoding == 6:
                # DCB with right
                # between;B;C;D to:
                # 1 right;B;C
                # 2 right;C;D
                premise1 = ['right', premise[1], premise[2]]
                premise2 = ['right', premise[2], premise[3]]
            elif encoding == 7:
                # BCD with mix left & right
                # between;B;C;D to:
                # 1 left;B;C
                # 2 right;D;C
                premise1 = ['left', premise[1], premise[2]]
                premise2 = ['right', premise[3], premise[2]]
            elif encoding == 8:
                # DCB with mix left & right
                # between;B;C;D to:
                # 1 right;B;C
                # 2 left;D;C
                premise1 = ['right', premise[1], premise[2]]
                premise2 = ['left', premise[3], premise[2]]
            else:
                raise UnboundLocalError('A premise is lost in encoding')
            enc_task.append(premise1)
            enc_task.append(premise2)
        else:
            enc_task.append(premise)
    return enc_task


def encode_response(mm, solution_set):
    """
# TODO WRITE
    Parameters
    ----------
    mm : list(str)
        Mental model of spatial reasoning task.
    solution_set : dict
        Container for accepted answers for a spatial reasoning task.

    Returns
    -------
    bool
        If model prediction is a valid conclusion true, none otherwise.

    """
    if mm in solution_set:
        prediction = 'True'
    else:
        prediction = 'None'
    return prediction
