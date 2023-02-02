import numpy as np


def calcAccuracy(LPred, LTrue):
    """Calculates prediction accuracy from data labels.

    Args:
        LPred (array): Predicted data labels.
        LTrue (array): Ground truth data labels.

    Retruns:
        acc (float): Prediction accuracy.
    """

    # --------------------------------------------
    # === Your code here =========================
    # --------------------------------------------
    # ============================================
    return np.mean(LPred == LTrue)


def calcConfusionMatrix(LPred, LTrue):
    """Calculates a confusion matrix from data labels.

    Args:
        LPred (array): Predicted data labels.
        LTrue (array): Ground truth data labels.

    Returns:
        cM (array): Confusion matrix, with predicted labels in the rows
            and actual labels in the columns.
    """

    # --------------------------------------------
    # === Your code here =========================
    # --------------------------------------------
    
    """
    matrixShit = np.zeros((2,2))
    for i in range(len(LPred)):
        if(LPred[i] == 1):
            if(LPred[i] == LTrue[i]):
                matrixShit[0,0] += 1
            else:
                matrixShit[1,0] += 1
        else:
            if(LPred[i] == LTrue[i]):
                matrixShit[1,1] += 1
            else:
                matrixShit[0,1] += 1
    
    
    cM = matrixShit
    print(cM)
    # ============================================
    """
    
    unique_labels = list(set(LTrue))
    num_labels = len(unique_labels)
    cM = np.zeros((num_labels, num_labels), dtype=int) 
    
    for i in range(len(LTrue)):
        cM[LPred[i], LTrue[i]] += 1
        
    return cM


def calcAccuracyCM(cM):
    """Calculates prediction accuracy from a confusion matrix.

    Args:
        cM (array): Confusion matrix, with predicted labels in the rows
            and actual labels in the columns.

    Returns:
        acc (float): Prediction accuracy.
    """

    # --------------------------------------------
    # === Your code here =========================
    # --------------------------------------------
    
    
    cM = sum(cM.diagonal())/cM.sum()
    print(cM)
    # ============================================
    
    return cM
