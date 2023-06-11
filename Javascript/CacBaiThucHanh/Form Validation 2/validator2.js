/*
-Tạo function Validator
-Lấy ra element `form` cần thực hiện validator
-Validator cho các thẻ input => lấy thẻ input nằm trong form có attribute là rules và name
-Tạo function trùng tên
-Lấy ra mảng ngăn cách nhau bởi dấu | và dấu :
-Cắt ra các rule rồi thì lấy ra rule ở bên trong function và map vào obj vào fromRules phải là array trong đó là func 
*/







function Validator(formSelector) {

    var _this = this;
    // Gán giá trị mặc định cho tham số khi định nghĩa
  
    // Func lấy trẻ cha

    function getParent(element, selector) {

        while (element.parentElement) {
            if (element.parentElement.matches(selector)) {
                return element.parentElement;
            }
            element = element.parentElement;
        }

    }

    // Tạo obj chứa tất cả rules của form
    var formRules = {};

    /*
     * Quy ước tạo rules:
     * - Nếu có lỗi return `error message`
     * - Nếu không có lỗi return `Undefined`
    */

    var validatorRules = {

        required: function(value) {
            // Sử dụng toán tử 3 ngôi nếu mà có value trả về undefine nếu không thì báo lỗi
            return value ? undefined : 'Vui lòng nhập trường này';
        },

        email: function(value) {
            // Biểu thức chính quy của email
            var regex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
            // Kiểu tra value đúng định dạng email thì trả về undefined
            return regex.test(value) ? undefined : 'Vui lòng nhập email';
        },

        min: function(min) {
            // Sử dụng function lồng nhau `Kết quả trả về của func thứ nhất sẽ là func thứ 2`
            // Nếu truyền số 6 vào min thì sẽ return ra func
            return function(value) {
                // Kiểm tra length của value có lơn hơn min hay không
                return value.length >= min ? undefined : `Vui lòng nhập ít nhất ${min} kí tự `;
            };
        },

        max: function(max) {
            return function(value) {
                return value.length <= min ? undefined : `Vui lòng nhập tối thiểu ${max} kí tự `;
            };
        }
    };




    // B1 Lấy ra element trong DOM theo `formSelector`
    var formElement = document.querySelector(formSelector);

    // B1 Chỉ xử lý khi có element trong DOM
    if (formElement) {
        //  B2 lấy các thẻ input trong form
        var inputs = formElement.querySelectorAll('[name][rules]')
        
        // Lặp qua các phần tử của Nodelist inputs
        for (var input of inputs) {
            
            // Lấy ra từng phần cách nhau bởi dấu | và gộp vào mảng
            var rules = input.getAttribute('rules').split('|');
            for (var rule of rules) {

                var ruleInfo;
                var isRuleHasValue = rule.includes(':')

                // Nếu mà rule includes chứa dấu : thì tách ra và đặt ra một biến khác\
                if (isRuleHasValue) {
                    ruleInfo = rule.split(':')
            
                    // Lấy chữ min gán vào rule
                    rule = ruleInfo[0];
                }
                var ruleFunction = validatorRules[rule];

                // Nếu mà có value thì gán lại ruleFunction có value
                if (isRuleHasValue) {
                    ruleFunction = ruleFunction(ruleInfo[1]);
                }
    
                // Kiểm tra xem formRules[input.name] có phải Array không
                // Lần đầu sẽ chạy ở else và gán nó là Array
                // Lần 2 là array rồi sẽ chạy điều kiện if rồi push vào
                // Lần 1 là gán required lần 2 sẽ gán còn lại
                if (Array.isArray(formRules[input.name])) {
                    formRules[input.name].push(ruleFunction)
                    
                } else {
                    // Lần đầu tiên sẽ đưa validator vào trong mảng `email : [f]`
                    formRules[input.name] = [ruleFunction];
                   
                }
            }
            /*
            Lấy ra attribute của input gán vào obj với dạng name: rules
            name là attribute hợp lệ nên có thể input.name còn rules tự định nghĩa phải dùng getAttribute
            formRules[input.name] = input.getAttribute('rules');
            */



            // Lắng nghe sự kiện để validate (blur, change, ....)
            input.onblur = handleValidate;
            input.oninput = handleClearError;

        };

        // Hàm thực hiện validate
        function handleValidate(event) {
            var rules = formRules[event.target.name];
            var errorMessage;

            for (var rule of rules) {
                errorMessage = rule(event.target.value);
                if (errorMessage) break;
            }
          

            // Nếu có lỗi hiển thị ra UI
            if (errorMessage) {
                var formGroup = getParent(event.target, '.form-group');
                
                if (formGroup) {
                    formGroup.classList.add('invalid');


                    var formMessage = formGroup.querySelector('.form-message');

                    if (formMessage) {
                        formMessage.innerText = errorMessage;
                    }
                }
            }

            return !errorMessage;
        }


        // Hàm clear Message lỗi
        function handleClearError(event) {
            var formGroup = getParent(event.target, '.form-group');
            if (formGroup.classList.contains('invalid')) {
                formGroup.classList.remove('invalid');

                var formMessage = formGroup.querySelector('.form-message');
                if (formMessage) {
                    formMessage.innerText = '';
                }
            }

        }


    }



    // Xử lý hành vi submit form
    formElement.onsubmit = function (event) {
        event.preventDefault();

        var inputs = formElement.querySelectorAll('[name][rules]')
        var isValid = true; 
        for (var input of inputs) {
            if (!handleValidate({ target: input })) {
                isValid = false;
            }
        }
       
        // Khi không có lỗi thì submit form

        if (isValid) {
            if (typeof _this.onSubmit === 'function') {
                var enableInputs = formElement.querySelectorAll('[name]');

					// vÌ enableInputs là một NodeList mà NodeList lại không sử dụng được reduce
					// Chuyển nó thành Array để sử dụng được reduce
				var formValue = Array.from(enableInputs).reduce((values, input) => {
					// Reduce thành key:value vào object sau đó cuối cùng là return ra values là một object
					switch (input.type) {
						case 'radio':
							if (input.matches(':checked')) {
									alues[input.name] = input.value;
							}
							break;
						case 'checkbox':
								// Không checked thì cho value là một mảng
							if (!values[input.name]) values[input.name] = [];
								// Nếu checked thì push vào mảng
							if (input.checked) values[input.name].push(input.value);
								// Kiểm tra nếu là mảng rỗng thì gán là chuỗi ''
							if (values[input.name].length === 0) values[input.name] = '';
							break;
						case 'file':
								values[input.name] = input.files;
								break;
						default:
							values[input.name] = input.value;
					}
					return values;
				}, {});

                    // Gọi lại hàm onSubmit và trả về giá trị của
                    _this.onSubmit(formValue);
            } else {
                formElement.submit();
            }
        }
    }
}