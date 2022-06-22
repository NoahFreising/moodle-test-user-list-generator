# Generate a csv file for importing users into Moodle
# Example structure of csv file:
# username,firstname,lastname,email
# student1,Student,One,s1@example.com
# student2,Student,Two,s2@example.com

if(__name__=='__main__'):
    import csv
    import os
    import sys
    import argparse

    # Parse arguments
    parser = argparse.ArgumentParser(description='Generate a csv file for importing users into Moodle')
    parser.add_argument('-u', '--username', help='Base username of the Moodle user', required=True)
    parser.add_argument('-n', '--number', help='Number of users to generate', required=True)
    parser.add_argument('-f', '--firstname', help='Firstname of the Moodle user', required=True)
    parser.add_argument('-l', '--lastname', help='Base lastname of the Moodle user', required=True)
    parser.add_argument('-e', '--email', help='Email domain of the Moodle user', required=True)
    parser.add_argument('-x', '--prefix', help='Prefix of the Moodle user email', required=True)
    parser.add_argument('-p', '--password', help='Password of the Moodle user', required=True)
    parser.add_argument('-o', '--output', help='Output file', required=True)
    args = parser.parse_args()

    # Check if output file exists
    if(os.path.isfile(args.output)):
        print('Output file already exists. Please remove it before running this script.')
        sys.exit(1)

    # Check if output file can be created
    try:
        f = open(args.output, 'w')
        f.close()
    except:
        print('Could not create output file. Please check if you have write permissions.')
        sys.exit(1)

    # Generate csv file
    with open(args.output, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['username', 'firstname', 'lastname', 'email', 'password'])
        for i in range(int(args.number)):
            writer.writerow([args.username + str(i), args.firstname, args.lastname + str(i), args.prefix + str(i) + args.email, args.password])

    print('Generated csv file: ' + args.output)
    sys.exit(0)