import yaml

try:
    stream = file('config.yaml', 'r')
    config = yaml.load(stream)

    print config
    print yaml.dump(config)

    yaml.dump(config, file('config_bak.yaml', 'w'))
except yaml.YAMLError, exc:
    print "Error in config.yaml"
    if hasattr(exc, 'problem_mark'):
        mark = exc.problem_mark
        print "Error position:  (line:%s, column:%s)" %(mark.line+1, mark.column+1)



