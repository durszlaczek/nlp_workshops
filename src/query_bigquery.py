import csv, argparse
from google.cloud import bigquery # pip install --upgrade google-cloud

client = bigquery.Client()  # authorize with Google Cloud (set GOOGLE_APPLICATION_CREDENTIALS)
# https://cloud.google.com/docs/authentication/getting-started

COLUMNS = ['title', 'score', 'num_comments', 'created_utc']
TIMEOUT = 50  # in seconds


def get_subreddits(subreddit_name):
    QUERY_W_PARAM = (
        'SELECT ' + ', '.join(COLUMNS) + ' '
        'FROM `fh-bigquery.reddit_posts.2017_*` '
        'WHERE subreddit = @subreddit ')

    param = bigquery.ScalarQueryParameter('subreddit', 'STRING', subreddit_name)
    job_config = bigquery.QueryJobConfig()
    job_config.query_parameters = [param]
    query_job = client.query(
        QUERY_W_PARAM, job_config=job_config)  # API request - starts the query
    iterator = query_job.result(timeout=TIMEOUT)
    rows = list(iterator)

    print('Query completed.')

    return rows


def save_rows(rows, filename):
    with open(filename, 'w') as output:
        writer = csv.writer(output)
        writer.writerow(COLUMNS)
        for row in rows:
            writer.writerow([row[0], row[1], row[2], row[3]])


def process_subreddit(subreddit_name, data_path):
    news = get_subreddits(subreddit_name)
    save_rows(news, data_path + subreddit_name + '.csv')

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--outfile', type=str,
                        help='A folder where data will be downloaded.', 
                        default='./data/')
    parser.add_argument('--subreddit', type=str,
                        help='Subreddit name. Check out here: https://www.reddit.com/subreddits', 
                        default='gaming')
    args = parser.parse_args()
    
    print('Processing', args.subreddit)
    process_subreddit(args.subreddit, args.outfile)

