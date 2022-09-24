const add_button = document.getElementById('add-service')
const template_div = document.getElementById('template-div')
const template_element = template_div.firstElementChild.cloneNode(true)
const csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value

function addPricing(client_name, services_object) {
    const payload = {
        'client_name': client_name,
        'services': services_object
    }
    fetch('add-pricing/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": csrf_token,
        },
        body: JSON.stringify(payload)
    }).then(res => res.json())

        .then(data => {
            window.location.href = '/pricing/' + data['pricing_id']
        })

        .catch(error => {
            console.log(error);
        })
}


let counter = 1
add_button.addEventListener('click', function (event){
    const new_element = template_element.cloneNode(true)
    const counter_el = new_element.firstElementChild.firstElementChild
    counter++
    counter_el.innerText = String(counter) + '.'
    template_div.appendChild(new_element)
})


const sum_button = document.getElementById('sum-button')
sum_button.addEventListener('click', function (e){
    const client_name = document.getElementById('id_client_name').value
    let services_array = []
    for (var i = 0, childNode; i < template_div.children.length; i ++) {
        const childNode = template_div.children[i]
        const service = childNode.querySelector('select')
        const quantity = childNode.querySelector('input')
        let temp_dict = {
            'service_id': service.value,
            'quantity': quantity.value
        }
        services_array.push(temp_dict)
    }
    addPricing(client_name, services_array)
})

