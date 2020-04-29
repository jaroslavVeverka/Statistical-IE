def viterbi(obs, states, start_p, trans_p, emit_p):
    V=[{}]
    for i in states:
        V[0][i]=start_p[i]*emit_p[i][obs[0]]
    # Run Viterbi when t > 0
    for t in range(1, len(obs)):
        V.append({})
        for y in states:
            (prob, state) = max((V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states)
            V[t][y] = prob
        for i in dptable(V):
            print (i)
        opt=[]
        for j in V:
            for x,y in j.items():
                if j[x]==max(j.values()):
                    opt.append(x)
    #the highest probability
    h=max(V[-1].values())
    print ('The steps of states are '+' '.join(opt)+' with highest probability of %s'%h)
    #it prints a table of steps from dictionary

def dptable(V):
    yield " ".join(("%10d" % i) for i in range(len(V)))
    for y in V[0]:
        yield "%.7s: " % y+" ".join("%.7s" % ("%f" % v[y]) for v in V)

states = ('P', 'T', 'O')
observations = ('flight', 'from', 'london', 'to', 'paris')
start_probability = {'P': 0.1, 'T': 0, 'O': 0.9}
transition_probability = {
    'P': {'P': 0.1, 'T': 0, 'O': 0.9},
    'T': {'P': 0, 'T': 0, 'O': 1},
    'O': {'P': 0.1, 'T': 0, 'O': 0.9}
}
emission_probability = {
    'P': {'airport': 0.05, 'central': 0, 'city': 0, 'delayed': 0, 'flight': 0, 'from': 0, 'is': 0.1, 'london': 0, 'of': 0.1, 'paris': 0, 'to': 0.3},
    'T': {'airport': 0.05, 'central': 0.1, 'city': 0, 'delayed': 0, 'flight': 0, 'from': 0, 'is': 0, 'london': 0.1, 'of': 0, 'paris': 0.1, 'to': 0},
    'O': {'airport': 0.01, 'central': 0.02, 'city': 0.03, 'delayed': 0.005, 'flight': 0.01, 'from': 0.05, 'is': 0.1, 'london': 0.01, 'of': 0.1, 'paris': 0.01, 'to': 0.1}
}

viterbi(observations, states, start_probability, transition_probability, emission_probability)