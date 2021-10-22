import numpy as np

class MarkovChain(object):
    """
    > init
    > next_state:: determina qual o próximo estado
    > generate_states:: gera uma seqüência de estados
    """


    def __init__(self, transition_matrix, states):
        """
        transition_matrix [dict] => {'state1': {'state1': prob11,
                                                'state2': prob12, ...},
                                     'state2': {'state1': prob21, ...}
                                     ....
                                     }
        """
        self.transition_matrix = np.atleast_2d(transition_matrix)
        self.states = states
        self.index_dict = {self.states[index]: index for index in range(len(self.states))}
        self.state_dict = {index: self.states[index] for index in range(len(self.states))} 


    def next_state(self, current_state):
        """
        Retornar o estado de uma variável aleatória no próximo instante de tempo.

        Parameters
        ----------
        current_state: str
            É o estado atual do sistema.
        """
        p = self.transition_matrix[self.index_dict[current_state], :]
        return np.random.choice(self.states, p=p)


    def generate_states(self, current_state, no=20):
        """
        Gerar o estado da variável aleatória no próximo instante
        
        Parameter
        ---------
        current_state [str]

        no [int] - option
            Número de estados gerados

        >>> generate_states('state1')
            state1, state1, state2, state3, state1 ...

        """

        _future_states = []

        for _ in range(no):
            next_state = self.next_state(current_state)
            _future_states.append(next_state)
            current_state = next_state

        return _future_states

    
    def is_accessible(self, state_i, state_f):
        """
        Checar se o state_f é acessível a partir do state_i

        Parameters
        ----------
        state_i [str]
            estado a partir do qual estamos checando a acessivilidade
        state_f [str]
            estado para o qual estamos testando a acessibilidade

        return [bool]
        """
        pass        

















