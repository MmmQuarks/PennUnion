from scipy import stats
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import streamlit as st


votes_cast = int( st.number_input("votes cast?") )
yes = int( st.number_input("yes votes?"))
no = int( st.number_input("no votes?"))
votes_counted = yes + no
votes_to_count = votes_cast - votes_counted

if votes_cast > 0 and yes > 0 & no >= 0:
    # k = number of yes votes
    # n = total number of trials
    # p = probability of yes votes
    
    p = yes / votes_counted
    pdf = stats.binom.pmf
    
    df = pd.DataFrame()
    df['yes_votes_remaining'] = list(range(0, votes_to_count+1))
    df['prob'] = pdf(k = df.yes_votes_remaining, n = votes_to_count, p = p)
    df['yes_votes'] = df['yes_votes_remaining'] + yes
    df['prob'] /= df.prob.sum()
    
    fig, ax = plt.subplots()
    ax.plot(
        df.yes_votes,
        df.prob
    )
    ax.set_xlabel('Total Yes Votes')
    ax.set_ylabel('Probability')
    
    victory = round(0.5 * votes_cast +1)
    victory_prob = np.round(
        df.loc[ df.yes_votes >= victory, 'prob'].sum(), 2
    )
    
    ax.set_title('Victory Probability = {}'.format(victory_prob))
    
    st.pyplot(fig)
