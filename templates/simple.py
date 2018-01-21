labels = [dict(name='design', color='yellow'),
          dict(name='documentation', color='green'),
          dict(name='development', color='yellow'),
          dict(name='test', color='yellow'),
          dict(name='planing', color='green'),
          dict(name='requirement', color='green'),
          dict(name='analysis', color='green'),
          dict(name='deployment', color='red'),
          ]

milestones = [dict(title='Configuration'),
              dict(title='Analysis'),
              dict(title='Development'),
              dict(title='Testing'),
              dict(title='Staging Deployment'),
              ]

issues = {
    'Configuration': [
        dict(title='Infrastructure Connectivity', labels=['design'])
    ],
    'Analysis': [
        dict(title='Gathering Business Requirements', labels='requirement,, design'),
        dict(title='Design Service Catalog', labels='design, analysis'),
        dict(title='Design Service Registry', labels='design, analysis'),
    ],
    'Development': [
        dict(title='add models', labels='development'),
        dict(title='add controller', labels='development'),
        dict(title='UI layout', labels='development'),
        dict(title='Home page', labels='development'),
        dict(title='Unit test', labels='development'),
        dict(title='Middleware ', labels='development')
    ],
    'Testing': [
        dict(title='Test',
             labels='test')
    ],
    'Staging Deployment': [
        dict(title='Package Deployment',
             labels='deployment')
    ],
    'Production Deployment': [
        dict(title='Package Deployment',
             labels='deployment')
    ]}
