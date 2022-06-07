import json
import yaml


def my_func(input_file, output_file):
  try:
    with open(input_file, 'r') as j:
      with open(output_file, "w") as y:
        json_data = json.loads(j.read())
        converted_data = json.dumps(json_data)

        yaml_data = yaml.safe_load(converted_data)
        converted_yaml_data = yaml.dump(yaml_data)
        y.write(converted_yaml_data)
        
  except FileNotFoundError:
    print("The file is not found!")
  except json.decoder.JSONDecodeError:
    print("The file format is not properly!")

  else:
    print("Success")

my_func("project2.json", "task_yaml.yaml")


