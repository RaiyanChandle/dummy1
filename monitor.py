from pathlib import Path

import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset


def main():
    # Reference dataset: baseline behaviour
    reference_data = pd.DataFrame({
        "feature": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19] * 10
    })

    # Current dataset: behaviour has shifted
    current_data = pd.DataFrame({
        "feature": [50, 51, 52, 53, 54, 55, 56, 57, 58, 59] * 10
    })

    # Create a data-drift report
    report = Report(
        metrics=[
            DataDriftPreset()
        ]
    )

    # Compare the reference and current datasets
    result = report.run(
        reference_data=reference_data,
        current_data=current_data
    )

    # Save the report as HTML
    reports_dir = Path("reports")
    reports_dir.mkdir(parents=True, exist_ok=True)

    report_path = reports_dir / "data_drift.html"
    result.save_html(str(report_path))

    print("Evidently monitoring completed.")
    print(f"Report saved to: {report_path.resolve()}")


if __name__ == "__main__":
    main()