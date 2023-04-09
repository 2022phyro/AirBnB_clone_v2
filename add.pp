exec {'Edit config file':
  command  => 'sudo sed -i "s/# pass PHP scripts to FastCGI server/location \/hbnb_static \{\n\t\talias \/data\/web_static\/current\/;\n\t\}\n\t# pass PHP scripts to FastCGI server/" mmm',
  provider => shell,
}
