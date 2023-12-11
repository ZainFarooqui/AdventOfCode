const fs = require('fs')

const EXPANSION_FACTOR = 1000000;

const readFile = (filePath) => {
    let data = [];
    try {
        const rawFile = fs.readFileSync(filePath, 'utf-8');
        const file = rawFile.split('\n')
        for (let line of file) {
           const curr = [];
            for (let char of line) {
                curr.push(char);
           };
           data.push(curr)
        };
    } catch (e) {
        console.log(e);
    };

    return data;
};

const findEmptyRows = (gMap, limit) => {
    const emptyRows = [];
    for (let i = 0; i < limit; i++) {
        if (gMap[i].every(el => el === '.')) emptyRows.push(i);
    };
    return emptyRows;
};

const findEmptyCols = (gMap, limit) => {
    const emptyCols = [];
    for (let i = 0; i < limit; i++) {
        const col = [];
        for (let row of gMap) {
            col.push(row[i]);
        };
        if (col.every(el => el === '.')) emptyCols.push(i);
    };
    return emptyCols;
};

const findEmptySpace = (gMap) => {
    const n = gMap.length;
    const m = gMap[0].length;

    const emptyRows = findEmptyRows(gMap, n);
    const emptyCols = findEmptyCols(gMap, m);
   
    return [emptyCols, emptyRows];
};

const findGalaxies = (cMap) => {
    const allGalaxies = [];
    for (let i = 0; i < cMap.length; i++) {
        for (let j = 0; j < cMap[0].length; j++) {
            if (cMap[i][j] === '#') allGalaxies.push([i, j]);
        };
    };

    return allGalaxies;
};

const findAllDistances = (gLocations, emptySpace) => {
    const emptyCols = emptySpace[0];
    const emptyRows = emptySpace[1];
    const expansionConstant = EXPANSION_FACTOR - 1;

    let sumOfDistances = 0;
    for (let i = 0; i < gLocations.length; i++) {
        for (let j = i + 1; j < gLocations.length; j++) {
            const startRow = Math.min(gLocations[i][0], gLocations[j][0]);
            const endRow = Math.max(gLocations[i][0], gLocations[j][0]);
            const startCol = Math.min(gLocations[i][1], gLocations[j][1]);
            const endCol = Math.max(gLocations[i][1], gLocations[j][1]);
           
            let numberOfEmptyRows = emptyRows.filter(el => (startRow < el && el < endRow)).length;
            let numberOfEmptyCols = emptyCols.filter(el => (startCol < el && el < endCol)).length;

            const distance = Math.abs(gLocations[j][0] - gLocations[i][0]) + 
                Math.abs(gLocations[j][1] - gLocations[i][1]) +
                numberOfEmptyCols * expansionConstant +
                numberOfEmptyRows * expansionConstant;

            sumOfDistances += distance
        };
    };

    return sumOfDistances;
};

const filePath = 'input.txt';
const data = readFile(filePath);
const emptySpace = findEmptySpace(data);
const galaxyLocations = findGalaxies(data);

const totalDistance = findAllDistances(galaxyLocations, emptySpace);

console.log(totalDistance);