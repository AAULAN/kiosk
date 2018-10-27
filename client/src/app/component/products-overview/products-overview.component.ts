import { SaleService } from './../../service/sale.service';
import { ProductService } from './../../service/product.service';
import { Component, OnInit, EventEmitter, Output, OnDestroy } from '@angular/core';
import { Product } from 'src/app/model/product.model';
import { MatSnackBar } from '@angular/material';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-products-overview',
  templateUrl: './products-overview.component.html',
  styleUrls: ['./products-overview.component.scss']
})
export class ProductsOverviewComponent implements OnInit, OnDestroy {
  displayedColumns: string[] = ['id', 'name', 'category', 'price', 'actions'];
  products = [];

  @Output() selectProduct = new EventEmitter();

  productUpdateSubscription: Subscription;

  constructor(private productService: ProductService,
              private saleService: SaleService,
              private snackBar: MatSnackBar) { }

  ngOnInit(): void {
    this.loadProducts();

    this.productUpdateSubscription = this.productService.productsUpdated$.subscribe(_ => this.loadProducts());
  }

  ngOnDestroy(): void {
    this.productUpdateSubscription.unsubscribe();
  }

  loadProducts() {
    this.productService.getAll().subscribe(data => this.products = data);
  }

  editProduct(product: Product) {
    this.selectProduct.emit(product);
  }

  deleteProduct(product: Product) {
    this.productService.delete(product).subscribe(() => {
      this.productService.notifyUpdate();
    }, error => {
      this.snackBar.open(`Could not delete the product 🤔 (${error.status})`);
    });
  }

  purchaseProduct(product: Product) {
    this.saleService.performSale(product).subscribe(() => {
      this.saleService.notifyUpdate();

      this.snackBar.open('Sale completed! 🎉');
    }, error => {
      this.snackBar.open(`Could not complete the sale 🤔 (${error.status})`);
    });
  }
}
