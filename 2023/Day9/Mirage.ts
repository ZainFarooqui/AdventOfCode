import * as fs from 'fs';

const loadFile = (filePath: string) => {
    let file: string[] = []
    try {
        const rawFile = fs.readFileSync(filePath, 'utf8');
        file = rawFile.split('\n')
    } catch (e) {
        console.log('error');
    };
    return file
};

const getNextValue = (line: string) => {
    const values: number[] = line.split(' ').map(el => Number(el));
    let tempValues: number[] = [...values];
    const endValues: number[] = [values[values.length -1]];
    const allEqual = (arr: number[]) => arr.every( (v: number) => v === arr[0]);

    while (!allEqual(tempValues)) {
        const differences: number[] = [];
        for (let i = 1; i <= tempValues.length-1; i ++) {
            differences.push(tempValues[i] - tempValues[i-1]);
        }
        tempValues = [...differences];
        endValues.push(tempValues[tempValues.length - 1]);
    }
    
    let nextValue = 0;
    for (let i =  endValues.length - 1; i > 0; i--) {
        nextValue += endValues[i];
    }

    return endValues[0] + nextValue;  
};

const getSumOfNext = (data: string[]) => {
    let sum: number = 0;

    for (const line of data) {
        const nextValue = getNextValue(line);
        sum = sum + nextValue;
    }

    return sum;
}

const getPrevValue = (line: string) => {
    const values: number[] = line.split(' ').map(el => Number(el));
    let tempValues: number[] = [...values];
    const startValues: number[] = [values[0]];
    const allEqual = (arr: number[]) => arr.every( (v: number) => v === arr[0]);

    while (!allEqual(tempValues)) {
        const differences: number[] = [];
        for (let i = 1; i <= tempValues.length-1; i ++) {
            differences.push(tempValues[i] - tempValues[i-1]);
        }
        tempValues = [...differences];
        startValues.push(tempValues[0]);
    }

    startValues.reverse();
    let curr = startValues[0];
    for (let i = 1; i < startValues.length; i++) {
        curr = startValues[i] - curr;
    }
    return curr
}

const getSumOfPrev = (data: string[]) => {
    let sum: number = 0;

    for (const line of data) {
        const nextValue = getPrevValue(line);
        sum = sum + nextValue;
    }

    return sum;
    
}

const filePath = 'input.txt';
const rawData = loadFile(filePath);
console.log(getSumOfPrev(rawData));