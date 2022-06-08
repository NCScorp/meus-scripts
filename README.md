O presente script necessita do selenium para que possa ser rodado sem problemas, então:

```pip install selenium```

Para que o Selenium funcione sem problemas, é necessário que algum driver de browser esteja instalado tbm na sua máquina:

- Chrome:	https://sites.google.com/chromium.org/driver/
- Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
- Firefox:	https://github.com/mozilla/geckodriver/releases
- Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/

Depois da instalação e de baixar o driver, em seu terminal utilize o comando ```whereis chromedriver``` e se você instalou tudo certo no terminal irá
aparecer o caminho de onde está instalado. Esse caminho deve ser informado no selenium quando for utilizar o driver escolhido, para mais detalhes acesse:
[Tutorial selenium](https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test) caso haja algum erro com driver e [Documentação selenium](https://selenium-python.readthedocs.io/installation.html)
