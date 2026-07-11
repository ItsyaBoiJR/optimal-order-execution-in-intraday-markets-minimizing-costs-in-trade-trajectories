# Optimal Order Execution in Intraday Markets: Minimizing Costs in Trade Trajectories

This repository contains a Python/PyTorch implementation of the methods proposed in the research paper [Optimal Order Execution in Intraday Markets: Minimizing Costs in Trade Trajectories](https://arxiv.org/pdf/2009.07892v2) by Christopher Kath and Florian Ziel. The paper addresses the problem of optimal execution in continuous intraday electricity markets, introducing a model to minimize trading costs while considering market conditions, order book depth, and time-to-delivery constraints.

## Overview

### Problem Statement
In intraday electricity markets, traders face the challenge of executing trades in a cost-effective manner. Factors such as market liquidity, timing, and price impact significantly influence the trading costs. The research explores strategies to:
- Decide whether to trade volumes at once or split orders into smaller pieces.
- Optimize execution trajectories while considering market-specific properties like order book depth and trading regimes (e.g., XBID).

The paper provides a refined optimization approach that outperforms simple benchmark models and demonstrates a significant monetary impact through optimal execution strategies.

### Key Contributions
1. Development of a cost-minimization model tailored for intraday electricity markets.
2. Incorporation of order book depth, time-to-delivery, and trading regimes into the execution strategy.
3. Out-of-sample study comparing benchmark models with the proposed optimization approach, demonstrating its effectiveness.

---

## Repository Contents

This repository provides an implementation of the proposed model and related benchmark strategies. It allows users to simulate and evaluate the performance of different trading strategies in an intraday market context.

### Code Structure
```
.
├── data/
│   ├── sample_data.csv         # Example market data for testing the implementation
├── models/
│   ├── benchmark_model.py      # Implementation of simple benchmark strategies
│   ├── optimization_model.py   # Implementation of the proposed optimization model
├── notebooks/
│   ├── data_preprocessing.ipynb # Notebook for preparing and analyzing the input data
│   ├── model_training.ipynb     # Notebook for training and evaluating the models
├── utils/
│   ├── data_loader.py          # Utilities for loading and preprocessing data
│   ├── metrics.py              # Functions to compute cost metrics and evaluate models
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## Getting Started

### Prerequisites
To run the code in this repository, you need the following:
- Python 3.8 or later
- PyTorch 1.12 or later
- Pandas, NumPy, Matplotlib, and other dependencies listed in `requirements.txt`

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/optimal-order-execution
   cd optimal-order-execution
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. **Prepare the data**: Use the provided `data_preprocessing.ipynb` notebook to preprocess market data and prepare it for the models.
2. **Train and evaluate models**: Open the `model_training.ipynb` notebook to train the benchmark and optimization models and evaluate their performance.
3. **Customize the model**: Modify the `optimization_model.py` script to adapt the optimization strategy to your specific market data or trading requirements.

---

## Core Concepts

### 1. Benchmark Models
The benchmark models include straightforward trading strategies, such as:
- **Immediate Execution**: Execute the entire volume at the current market price.
- **Uniform Slicing**: Split the order volume into equal parts and execute them over a fixed time interval.

These models serve as a baseline to compare against the proposed optimization-based approach.

### 2. Optimization Model
The optimization model implements a refined cost-minimization strategy that:
- **Incorporates Order Book Depth**: Adjusts trading based on the market's liquidity levels.
- **Accounts for Time-to-Delivery**: Optimizes the execution trajectory based on the remaining time until delivery.
- **Considers Trading Regimes**: Adapts trading behavior for specific market conditions (e.g., XBID rules).

### 3. Evaluation Metrics
The models are evaluated using metrics such as:
- **Total Execution Cost**: The total monetary cost incurred during the execution process.
- **Price Impact**: The effect of executed trades on the market price.
- **Execution Efficiency**: Comparison of actual costs against theoretical minimum costs.

---

## Results
The implementation allows users to reproduce the results presented in the paper, including:
- Comparative analysis of benchmark models and the optimization approach.
- Visualizations of trade trajectories and cost breakdowns.
- Insights into how market conditions influence the effectiveness of different strategies.

---

## Future Work
While the current implementation focuses on intraday electricity markets, the framework can be extended to:
- Other continuous trading markets (e.g., equities or commodities).
- More complex optimization objectives, such as risk-adjusted execution strategies.

---

## References
If you find this repository useful, please consider citing the original paper:
```
@article{kath2020optimal,
    title={Optimal Order Execution in Intraday Markets: Minimizing Costs in Trade Trajectories},
    author={Christopher Kath and Florian Ziel},
    journal={arXiv preprint arXiv:2009.07892v2},
    year={2020},
    url={https://arxiv.org/pdf/2009.07892v2}
}
```

---

## License
This repository is licensed under the MIT License. See the `LICENSE` file for more details.

For questions or feedback, feel free to open an issue or contact the repository maintainers.