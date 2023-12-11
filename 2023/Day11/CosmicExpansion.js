const fs = require('fs')

const EXPANSION_FACTOR = 1000000

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

const formatGalaxy = (gMap) => {
    const n = gMap.length;
    const m = gMap[0].length;

    const emptyRows = findEmptyRows(gMap, n);
    const emptyCols = findEmptyCols(gMap, m);
    
    const newMap = [];
    for (let i = 0; i < n; i++) {
        const newRow = []
        for (let j = 0; j < m; j++) {
            newRow.push(gMap[i][j]);
            if (emptyCols.includes(j)) {
                newRow.push('.')
            };
        };
        newMap.push(newRow)

        if (emptyRows && emptyRows[0] === i) {
            const fillRow = Array(n).fill('.');
            newMap.push(fillRow);
            emptyRows.shift()
        };
    };
    return newMap
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

const findAllDistances = (gLocations) => {
    let sumOfDistances = 0;
    for (let i = 0; i < gLocations.length; i++) {
        for (let j = i + 1; j < gLocations.length; j++) {
            const distance = Math.abs(gLocations[j][0] - gLocations[i][0]) + 
                                Math.abs(gLocations[j][1] - gLocations[i][1]);
            sumOfDistances += distance
        };
    };

    return sumOfDistances;
};

const filePath = 'example.txt';
const data = readFile(filePath);
const cosmicMap = formatGalaxy(data);
const galaxyLocations = findGalaxies(cosmicMap);
const totalDistance = findAllDistances(galaxyLocations);

console.log(totalDistance);