import { Component } from '@angular/core';
import { Product } from '../model/product.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'Kiosk';

  selectedProduct: Product;

  selectProduct(product: Product) {
    this.selectedProduct = product;
  }

  createProduct() {
    this.selectedProduct = new Product();
  }
}
