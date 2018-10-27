import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Sale } from '../model/sale.model';
import { Product } from '../model/product.model';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class SaleService {

  private api = `${environment.apiBase}/sales`;

  constructor(private client: HttpClient) { }

  performSale(product: Product, amount: number = 1) {
    const sale = new Sale();
    sale.productId = product.id;
    sale.amount = amount;

    return this.client.post<any>(this.api, sale);
  }
}
