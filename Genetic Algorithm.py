import numpy as np

# intial population
populationSize = 6
population = np.random.randint(0, high=30, size=(populationSize,4), dtype=int)
print('The Initial Population: \n', population)
found = False
generation = 1

while found == False:    
    # Evaluation function
    F_obj = [abs(chromosome[0] + 2*chromosome[1] + 3*chromosome[2] + 4*chromosome[3] - 30) for chromosome in population]
    
    # check if the obj is the goal
    if 0 in F_obj:
        print('Number Of Generations: ', generation)
        index = F_obj.index(0)
        print('Goal: ', population[index])
        found = True
        break
    # Fitness function
    fitness = [1/(obj+1) for obj in F_obj]
    total = sum(fitness)
    chromosomeProbabilities = fitness/total
    
    # selection using Roulette Wheel Selection
    selectCrIndex = np.random.choice(6, 6, p=chromosomeProbabilities)
    selectedCr = [population[index] for index in selectCrIndex]
    selectedCr = np.array(selectedCr)
    
    # Choosing parents by Crossover-Rate
    rand = np.random.random(populationSize)
    crossOverRate = 0.25
    pSelect = rand < crossOverRate
    parents = selectedCr[[(i == True) for i in pSelect]]
    parentsC = parents.copy()
    
    # one-cut point Cross Over 
    crossOverCutPoint = np.random.randint(1,3,len(parents))
    if len(parents) > 1:
        for i in range(len(parents)):
            crossPoint = crossOverCutPoint[i]
            if i == len(parents) - 1:
                parents[i, crossPoint:] = parentsC[0, crossPoint:]
            else:
                parents[i, crossPoint:] = parentsC[i+1, crossPoint:]
                
    # Replacing new parents
    Index = 0
    for index,p in enumerate(pSelect):
        if p == True:
            selectedCr[index,:] = parents[Index,:] 
            Index += 1
            
    # Checking for mutation
    ChromosomeNum = 6
    genotypeNum = 4
    totalGenes = ChromosomeNum * genotypeNum
    mutationRate = 0.2
    mutationSize = int(totalGenes * mutationRate)
    rand = np.random.randint(1, high=totalGenes, size = mutationSize, dtype=int)
    for i in rand:
        if i % genotypeNum != 0:
            row = int(i / genotypeNum)
            index = (i % genotypeNum) - 1
        else:
            row = int(i / genotypeNum) - 1
            index = genotypeNum -1
        selectedCr[row][index] = np.random.randint(0, high=30, dtype=int)
    population = selectedCr
    
    generation += 1