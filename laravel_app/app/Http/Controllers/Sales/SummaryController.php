<?php

namespace App\Http\Controllers\Sales;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;

class SummaryController extends Controller
{
    public function index(Request $request)
    {
        $response = Http::get('http://fastapi_app/sales-summary', [
            'start_date' => $request->start_date,
            'end_date' => $request->end_date,
            'category' => $request->category,
            'store_location' => $request->store_location,
        ]);

        $sales_summary = $response->json();

        return view('sales.index', compact('sales_summary'));
    }
}
