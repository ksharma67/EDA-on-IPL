def annot_plot(ax,w,h):                                    # function to add data to plot
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    for p in ax.patches:
        ax.annotate('{0:.1f}'.format(p.get_height()), (p.get_x()+w, p.get_height()+h))
        
class CricketDataHandling:
	def __init__(self, dataset):
		self.dataset = dataset

	def find_null_values(dataset):
		dataset.isnull().sum()
		num_null = dataset.isnull().sum().sum()
		print("No of Null Values: {}".format(num_null))

	def replace_values_for_consistency(dataset):
		dataset.replace( 'Rising Pune Supergiant', 'Rising Pune Supergiants',inplace = True)
		print(dataset.head(2))

	def replace_null_city_values(dataset):
		dataset['city'].fillna( dataset['venue'].apply(lambda x: x[:5]),inplace = True)
		dataset[dataset['city']== 'Dubai']

	def display_post_profiling(dataset):
		print(dataset.columns)
		print(dataset['team1'].unique())

	def matches_won_total_matches(dataset, matches_won, total_matches):
		matches_won = dataset.groupby('winner').count()
		matches_won
	
		total_matches = dataset['team1'].value_counts()+ dataset['team2'].value_counts()
		total_matches
	
		matches_won['Total matches']=total_matches
		matches_won[["Total matches","result"]].sort_values(by=["Total matches"],ascending=False).plot.bar(stacked=True,figsize=(7,3))

	def runs_scored_ascending(most_runs):
		asc_most_runs = most_runs.sort_values(by="total_runs", ascending=True)
		print(asc_most_runs)
	def runs_scored_descending(most_runs):
		desc_most_runs = most_runs.sort_values(by="total_runs", ascending=False)
		print(desc_most_runs)