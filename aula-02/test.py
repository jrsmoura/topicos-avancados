from markov_chain import MarkovChain as mc

def main():

    states = ['saudavel', 'doente', 'recuperado']
    prob_matrix = [[0.8, 0.2, 0.0],
                   [0.0, 0.7, 0.3],
                   [1.0, 0.0, 0.0]]

    system = mc(prob_matrix, states)
    next_state = system.next_state('saudavel')
#    print(next_state)
    system_evolution = system.generate_states(current_state='saudavel')
    print(system_evolution)


if __name__ == '__main__':
    main()
