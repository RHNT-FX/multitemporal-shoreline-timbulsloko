"""Accuracy checks and the uncertainty budget. Owner: M4.

See 03_EVALUATION_ANALYSIS.md for what each number means and how it is reported.
"""
import numpy as np


def confusion(true_labels: np.ndarray, predicted_labels: np.ndarray) -> np.ndarray:
    """2 x 2 confusion matrix with water as the positive class.

    Inputs:
        true_labels: True = water, from the labelled baseline points.
        predicted_labels: True = water, our mask read at the same points.

    Returns:
        [[TP, FN],
         [FP, TN]]
        TP = water called water, FN = water called land,
        FP = land called water, TN = land called land.
    """
    raise NotImplementedError("Not written yet - owner: M4")


def classification_metrics(confusion_matrix: np.ndarray) -> dict:
    """Accuracy numbers from a confusion matrix.

    Returns a dictionary with:
        overall_accuracy   = (TP + TN) / N, plus its 95% interval +/- 1.96 * sqrt(p * (1 - p) / N)
        precision          = TP / (TP + FP)   (user's accuracy for water)
        recall             = TP / (TP + FN)   (producer's accuracy for water)
        f1                 = 2 * precision * recall / (precision + recall)
        kappa              = Cohen's kappa
    Check: TP 90, FP 10, FN 5, TN 95 -> accuracy 0.925, precision 0.900, recall 0.947,
    f1 0.923, kappa 0.850.
    """
    raise NotImplementedError("Not written yet - owner: M4")


def cohen_kappa(labels_first: np.ndarray, labels_second: np.ndarray) -> float:
    """Cohen's kappa: agreement between two sets of labels, corrected for agreement by chance.

    kappa = (observed_agreement - chance_agreement) / (1 - chance_agreement)
    Used for the two annotators (50 shared points) and for map vs reference.
    """
    raise NotImplementedError("Not written yet - owner: M4")


def shoreline_errors(signed_distances_m: np.ndarray) -> dict:
    """Error numbers for extracted shoreline minus reference shoreline, along the transects.

    Returns a dictionary with:
        bias_m (mean signed distance; positive = our line is too far seaward),
        mae_m (mean absolute distance), rmse_m (root mean square), p95_m (95th percentile).
    """
    raise NotImplementedError("Not written yet - owner: M4")


def tide_error(tide_difference_m: float, tan_beta: float) -> float:
    """How far the waterline moves sideways because of a tide difference, in metres.

    = |tide_difference_m| / tan_beta, where tan_beta is the slope of the mudflat.
    """
    raise NotImplementedError("Not written yet - owner: M4")


def uncertainty_budget(position_error_m: float, registration_error_m: float,
                       tide_error_m: float) -> float:
    """Total shoreline uncertainty E = sqrt(position^2 + registration^2 + tide^2), in metres."""
    raise NotImplementedError("Not written yet - owner: M4")


def epr_uncertainty(error_start_m: float, error_end_m: float, years_between: float) -> float:
    """Uncertainty of the EPR rate = sqrt(error_start^2 + error_end^2) / years_between, in m/yr."""
    raise NotImplementedError("Not written yet - owner: M4")


def significant_change(nsm_m: np.ndarray, error_start_m: float, error_end_m: float) -> np.ndarray:
    """True for transects whose change is bigger than the uncertainty.

    significant = |NSM| > sqrt(error_start^2 + error_end^2)
    """
    raise NotImplementedError("Not written yet - owner: M4")
