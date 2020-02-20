var imported_module = require('./first.js')

console.log(imported_module)

/////////////////////////////////////
function test_scope (){
    var global = 'global string';

    function inner(){
        // 'let' defines a local variable that can only be accessed inside its scope.
        let local = 'local string';
        return (global + '\n' + local);
    }

    // This line won`t work.
    // console.log(local)
    return inner()
}

console.log(test_scope())
