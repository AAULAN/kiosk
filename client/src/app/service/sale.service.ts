import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Sale } from '../model/sale.model';
import { Product } from '../model/product.model';
import { HttpClient } from '@angular/common/http';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SaleService {
  private _salesUpdated = new Subject<void>();
  salesUpdated$ = this._salesUpdated.asObservable();

  private api = `${environment.apiBase}/sales`;

  constructor(private client: HttpClient) { }

  performSale(product: Product, amount: number = 1) {
    return this.client.post<any>(this.api, {product: product.id, amount: amount});
  }

  getAll() {
    return this.client.get<Sale[]>(this.api);
  }

  notifyUpdate() {
    return this._salesUpdated.next();
  }

  delete(sale: Sale) {
    return this.client.delete<any>(`${this.api}/${sale.id}`);
  }
}
