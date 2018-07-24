api = dict(
    private_token='<token_here>',
    base_url='<url_here>',
    base_path='api/v4'
)

# basics
headers = {'PRIVATE-TOKEN': api['private_token']}

# any project under group will not present in report
exclude_group = [57, 2, 106, 46]
