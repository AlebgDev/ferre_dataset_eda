from eda_ferro.load_csv import load_dataset
from eda_ferro.utils import summarize_data, plot_correlation, plot_distribution, count_categorical, plot_boxplot, time_distribution, price_duration

def main():
    dataset = "thegurus-opendata-renfe-trips.csv"
    df = load_dataset(dataset, sample_size=500000)
    summary = summarize_data(df)
    
    print("Resumen")
    print(summary)
    
    plot_correlation(df)
    plot_distribution(df)
    
    if 'duration' in df.columns:
        plot_boxplot(df, 'duration')
        
    if 'price' in df.columns:
        plot_boxplot(df, 'price')
    
    if 'company' in df.columns:
        count = count_categorical(df, 'company')
        print("Distribución de compañias")
        print(count)
        
    time_distribution(df)
    price_duration(df)
    
if __name__ == "__main__":
    main()