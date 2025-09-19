def safe_apply(func,data):
    results=[]
    errors=[]

    for element in data:
        try:
            result=func(element)
            results.append((element,result))
        except Exception as e:
            errors.append((element,type(e).__name__))

    return results, errors

sqrt=lambda x: float(x)**0.5 if float(x)>=0 else ValueError('Корень из отрицательного числа')
data=['4','16','text','-25','9.0',None]
results, errors=safe_apply(sqrt, data)
print('Результаты:')
for element, result in results:
    if not isinstance(result, ValueError):
        print(f'{element}={result}^2')
print('Ошибки:')
for element, error_type in errors:
    print(f'{element}: {error_type}')
for element, result in results:
    if isinstance(result, ValueError):
        print(f'{element}: {result}')