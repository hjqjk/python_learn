
//弹窗
alert('warning');

//会在浏览器的console中显示内容。主要用于调试
console.log("log message .......");

//变量和函数
//全局变量(建议用window.xxx来定义全局变量，以便和局部变量区分开来，不然出错时都不知什么原因)
window.name = 'hjq' ;

//js是先全编译，再执行的。所以函数调用可以在函数定义之前使用，不会影响。注意，Python是不能这样做的！
f1(window.name)
f2()

//基本函数
function f1(name){
	console.log(name)
}

function f2(){
	//局部变量，必须用var指定。
	var name = 'jk'
	console.log(name)
}

//自执行函数，不用另外调用，会自动执行。还能传参数。还是不理解这个要用在哪里？
(function(mesg){
	console.log(mesg)
})('auto execute')






