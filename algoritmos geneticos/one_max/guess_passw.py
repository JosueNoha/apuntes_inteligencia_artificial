import datetime
import genetic
import unittest
import random

class GuessPasswordTests(unittest.TestCase):
    geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,"

    def guess_password(self,target):
        startTime = datetime.datetime.now()
        
        def fnGetFitness(genes): 
            return get_fitness(genes, target)
        def fnDisplay(candidate): 
            display(candidate, startTime)
            
        optimalFitness = len(target)
        best = genetic.get_best(fnGetFitness, len(target), optimalFitness, self.geneset, fnDisplay)
        self.assertEqual(''.join(best.Genes), target)
        
    def test_Hello_World(self):
        target = "Hello World!"
        self.guess_password(target)

    def test_For_I_am_ferfully_and_wonderfully_made(self):
        target = 'For I am fearfully and wonderdully made.'
        self.guess_password(target)

    def test_Random(self):
        length = 50
        target = ''.join(random.choice(self.geneset) for _ in range(length))
        self.guess_password(target)

    def test_benchmark(self):
        #genetic.Benchmark.run(self.test_For_I_am_ferfully_and_wonderfully_made)
        genetic.Benchmark.run(self.test_Random)

def get_fitness(genes,target):
    return sum(1 for expected, actual in zip(target,genes) if expected ==actual)


def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print('{0}\t{1}\t{2}'.format(''.join(candidate.Genes),candidate.Fitness,str(timeDiff)))
    
if __name__ == '__main__':
    unittest.main()

