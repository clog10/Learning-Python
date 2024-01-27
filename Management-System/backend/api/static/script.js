document.addEventListener("DOMContentLoaded", init);
const URL_API = 'http://localhost:3000/'

var customers = []

function init() {
    search()
}

function agregar() {
    clean()
    abrirFormulario()
}

function abrirFormulario() {
    htmlModal = document.getElementById("modal");
    htmlModal.setAttribute("class", "modale opened");
}

function cerrarModal() {
    htmlModal = document.getElementById("modal");
    htmlModal.setAttribute("class", "modale");
}


async function search() {
    var url = URL_API + 'academies'
    var response = await fetch(url, {
        "method": 'GET',
        "headers": {
            "Content-Type": 'application/json'
        }
    })
    academies = await response.json();

    var html = ''
    for (academy of academies) {
        var row = `<tr>
    <td>${academy.name}</td>
    <td>${academy.phone}</td>
    <td>${academy.website}</td>
    <td>
        <a href="#" onclick="edit(${academy.id})" class="myButton">Editar</a>
        <a href="#" onclick="remove(${academy.id})" class="btnDelete">Eliminar</a>
    </td>
  </tr>`
        html = html + row;
    }


    document.querySelector('#customers > tbody').outerHTML = html
}

function edit(id) {
    abrirFormulario()
    var academy = academies.find(x => x.id == id)
    document.getElementById('txtId').value = academy.id
    document.getElementById('txtName').value = academy.name
    document.getElementById('txtPhone').value = academy.phone
    document.getElementById('txtWebsite').value = academy.website
}

async function remove(id) {
    respuesta = confirm('¿Está seguro de eliminarlo?')
    if (respuesta) {
        var url = URL_API + 'academy/' + id
        await fetch(url, {
            "method": 'DELETE',
            "headers": {
                "Content-Type": 'application/json'
            }
        })
        window.location.reload();
    }
}

function clean() {
    document.getElementById('txtId').value = ''
    document.getElementById('txtName').value = ''
    document.getElementById('txtPhone').value = ''
    document.getElementById('txtWebsite').value = ''
}

async function save() {
    var data = {
        "name": document.getElementById('txtName').value,
        "phone": document.getElementById('txtPhone').value,
        "website": document.getElementById('txtWebsite').value
    }

    var id = document.getElementById('txtId').value
    if (id != '') {
        data.id = id
    }

    var url = URL_API + 'academy'
    await fetch(url, {
        "method": 'POST',
        "body": JSON.stringify(data),
        "headers": {
            "Content-Type": 'application/json'
        }
    })
    window.location.reload();
}