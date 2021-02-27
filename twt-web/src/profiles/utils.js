import numeral from 'numeral'

export function num(number) {
    return numeral(number).format("0a")  
}
