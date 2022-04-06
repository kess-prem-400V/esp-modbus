from esp_docs.conf_docs import *  # noqa: F403,F401

extensions += ['sphinx_copybutton',
               # Needed as a trigger for running doxygen
               'esp_docs.esp_extensions.dummy_build_system',
               'esp_docs.esp_extensions.run_doxygen'
               ]

# link roles config
github_repo = 'espressif/esp-modbus'

# context used by sphinx_idf_theme
html_context['github_user'] = 'espressif'
html_context['github_repo'] = 'esp-modbus'

# Extra options required by sphinx_idf_theme
project_slug = 'esp-modbus'
versions_url = 'https://raw.githubusercontent.com/espressif/esp-modbus/master/docs/docs_versions.js'

idf_targets = ['esp32', 'esp32s2', 'esp32c3']
languages = ['en']
