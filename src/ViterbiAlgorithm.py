# implementace Viterbiho algoritmu
# obs - zpracovávaná posloupnost slov
# states - stavy HMM
# start_p - iniciační pravděpodobnosti
# trans_p - pravděpodobnosti přechodu
# emit_p - emisní pravděpodobnosti
def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}
    V = [{y: (start_p[y] * emit_p[y][obs[0]]) for y in states}]
    path = {y: [y] for y in states}

    for t in range(1, len(obs)):
        V.append({})
        newpath = {}

        for y in states:
            (prob, state) = max((V[t - 1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states)
            V[t][y] = prob
            newpath[y] = path[state] + [y]

        path = newpath

    print_dptable(V)
    (prob, state) = max((V[t][y], y) for y in states)
    return (prob, path[state])


# metoda pro vizualizaci řešení
def print_dptable(V):
    s = "    " + " ".join(("%7d" % i) for i in range(len(V))) + "\n"
    for y in V[0]:
        s += "%.5s: " % y
        s += " ".join("%.7s" % ("%f" % v[y]) for v in V)
        s += "\n"
    print(s)

# definice úlohy
states = ('P', 'T', 'O')
observations = ('flight', 'from', 'london', 'to', 'paris')
start_probability = {'P': 0.1, 'T': 0, 'O': 0.9}
transition_probability = {
    'P': {'P': 0, 'T': 1, 'O': 0},
    'T': {'P': 0, 'T': 0, 'O': 1},
    'O': {'P': 0.1, 'T': 0, 'O': 0.9}
}
emission_probability = {
    'P': {'airport': 0.05, 'central': 0, 'city': 0, 'delayed': 0, 'flight': 0, 'from': 0, 'is': 0.1, 'london': 0,
          'of': 0.1, 'paris': 0, 'to': 0.3},
    'T': {'airport': 0.05, 'central': 0.1, 'city': 0, 'delayed': 0, 'flight': 0, 'from': 0, 'is': 0, 'london': 0.1,
          'of': 0, 'paris': 0.1, 'to': 0},
    'O': {'airport': 0.01, 'central': 0.02, 'city': 0.03, 'delayed': 0.005, 'flight': 0.01, 'from': 0.05, 'is': 0.1,
          'london': 0.01, 'of': 0.1, 'paris': 0.01, 'to': 0.1}
}

# provedení úlohy
result = viterbi(observations, states, start_probability, transition_probability, emission_probability)
print(result)
