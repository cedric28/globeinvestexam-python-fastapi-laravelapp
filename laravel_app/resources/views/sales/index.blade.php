<!DOCTYPE html>
<html>
<head>
    <title>Sales Summary</title>
</head>
<body>
    <h1>Sales Summary</h1>
  <p>Total Sales: {{ $data['TotalSales'] }}</p>
    <h2>Top Products</h2>
    <ul>
        @foreach($data['TopProducts'] as $product)
        <li>{{ $product }}</li>
    @endforeach
    </ul>
</body>
</html>