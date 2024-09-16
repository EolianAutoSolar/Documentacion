.. Documentation documentation master file, created by
   sphinx-quickstart on Tue Sep 10 20:11:43 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentación proyecto Eolian
==================================

Este documento considera todos los elementos necesarios para la construcción del auto solar.

Para crear la documentación en la terminal:

Ir a la carpeta documentacion y ejecutar el archivo makefile con

.. code-block:: bash

   $make

.. code-block:: bash

   $sphinx-build -M html docs/source/ docs/build/

Documentacion makefile https://makefiletutorial.com/

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Arquitectura
   Electrica
   Mecánica
   .. Software
   .. Diseño
   .. Seguridad
   .. Pruebas
   .. Integración
   .. Mantenimiento
   .. Costos


