exec {'Edit config file':
  command  => "sudo sed -i '/# pass PHP scripts to FastCGI server/i \\tlocation \/hbnb_static \{\n\t\talias \/data\/web_static\/current\/;\n\t\}\n' mmm",
  provider => shell,
}
