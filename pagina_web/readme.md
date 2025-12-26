{% extends "base.html" %}

{% block content %}
<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="card shadow">
                <div class="card-body">
                    <h2 class="text-primary border-bottom pb-2">Acerca de MegaRegistros</h2>
                    <p class="lead">Este proyecto es una plataforma de gestión integral desarrollada para la entrega final del curso de Python/Django.</p>
                    
                    <h4 class="mt-4">Información del Proyecto</h4>
                    <ul class="list-group list-group-flush mb-4">
                        <li class="list-group-item"><strong>Nombre:</strong> MegaRegistros</li>
                        <li class="list-group-item"><strong>Objetivo:</strong> Facilitar la administración centralizada de datos corporativos.</li>
                    </ul>

                    <h4 class="mt-4">Descripción de Modelos (Punto 1 Consigna)</h4>
                    <p>El sistema utiliza los siguientes modelos para estructurar la información:</p>
                    <div class="accordion" id="accordionModelos">
                        <div class="accordion-item">
                            <h2 class="accordion-header">
                                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne">
                                    1. Empleado
                                </button>
                            </h2>
                            <div id="collapseOne" class="accordion-collapse collapse" data-bs-parent="#accordionModelos">
                                <div class="accordion-body">Gestiona los datos del personal, incluyendo nombres y cargos jerárquicos.</div>
                            </div>
                        </div>
                        <div class="accordion-item">
                            <h2 class="accordion-header">
                                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo">
                                    2. Producto
                                </button>
                            </h2>
                            <div id="collapseTwo" class="accordion-collapse collapse" data-bs-parent="#accordionModelos">
                                <div class="accordion-body">Permite administrar el inventario con nombres de productos y sus respectivos precios.</div>
                            </div>
                        </div>
                        <div class="accordion-item">
                            <h2 class="accordion-header">
                                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree">
                                    3. Cliente
                                </button>
                            </h2>
                            <div id="collapseThree" class="accordion-collapse collapse" data-bs-parent="#accordionModelos">
                                <div class="accordion-body">Centraliza la información de contacto y nombres de los clientes comerciales.</div>
                            </div>
                        </div>
                    </div>

                    <div class="mt-5 text-center p-3 bg-light rounded">
                        <h5>Desarrollado por:</h5>
                        <p class="mb-0"><strong>Magali Heinermann</strong></p>
                        <small>Estudiante de Data Science / Python - 2025</small>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}