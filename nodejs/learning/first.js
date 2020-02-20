function test_module (){
    function test(input) {
        var res = input ** 2;
        return res;
    };

    console.log(test(5));

    var data = require('./data.json');
    console.log(data["key0"]);
    console.log(data["key1"]);

    return "test string.\n"
};

exports.module = test_module();
