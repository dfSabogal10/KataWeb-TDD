__author__ = 'asistente'
from unittest import TestCase
from selenium import webdriver
import os.path
from selenium.webdriver.common.by import By

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(2000)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span=self.browser.find_element(By.XPATH, '//span[text()="David Felipe Sabogal"]')
        span.click()

        h2=self.browser.find_element(By.XPATH, '//h2[text()="David Felipe Sabogal"]')

        self.assertIn('David Felipe Sabogal', h2.text)

    def test_login(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()

        loginmodal=self.browser.find_element_by_id('login_modal')
        nombreUsuario = loginmodal.find_element_by_id('id_username')
        nombreUsuario.send_keys('felipe')


        clave = loginmodal.find_element_by_id('id_password')
        clave.send_keys('administrador')

        botonGrabar = self.browser.find_element_by_id('id_ingresar')
        botonGrabar.click()

        self.browser.implicitly_wait(3)
        linkeditar = self.browser.find_element_by_id('id_editar')
        self.assertIn('Editar', linkeditar.text)

    def test_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('David Felipe')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Sabogal')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('1')

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3001234567')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('df.sabogal10@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        print()
        imagen.send_keys(os.path.dirname(os.path.realpath(__file__))+'/static/atila.jpeg')
        registermodal=self.browser.find_element_by_id('register_modal')
        nombreUsuario = registermodal.find_element_by_id('id_username')
        nombreUsuario.send_keys('felipe1')

        clave = registermodal.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)
        span=self.browser.find_element(By.XPATH, '//span[text()="David Felipe Sabogal"]')

        self.assertIn('David Felipe Sabogal', span.text)

