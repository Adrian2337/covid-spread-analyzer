function jsonify(variable) {
    return JSON.parse(variable.replaceAll(/&quot;/ig, '"').replaceAll('&#x27;', '"'));
}

var voi_data = jsonify(data_raw) // dane dla wojewodztwa
console.log(voi_data)

