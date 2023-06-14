let arr = [0,2,5,1,5]

for (let pos = 0; pos < arr.length; pos++) {
    console.log(`A posição ${pos} tem o valor ${arr[pos]}`)
}

// nova forma
for (let pos in arr) {
    console.log(`A posição ${pos} tem o valor ${arr[pos]}`)
} 