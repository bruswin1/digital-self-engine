VALID={"strong_match","partial_match","deviation","unknown"}

def summarize(results):
    out={k:0 for k in VALID}
    for row in results:
        label=row.get("score","unknown")
        if label not in VALID: label="unknown"
        out[label]+=1
    return out
